import os
from datetime import date, timedelta, datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
# Only initialize Spark if testing locally
# Otherwise it should be already running within Spark
try:
    from pyspark import SparkContext
except ImportError:
    import spark_env

from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

IN_IPYTHON = True

try:
    __IPYTHON__
except NameError:
    IN_IPYTHON = False
    sc = SparkContext('local')
    print "Not in IPython, creating SparkContext manually"


def week_file(week):
    event_storage = os.path.join('___EVENT_STORAGE___', 'events-' + week + '.csv')

    # if not ipython that probably means you are not running this on a Spark Cluster
    # the telemetry spark cluster only supports uploading a ipynb.
    if not IN_IPYTHON:
        print 'Failed to find:' + event_storage
        event_storage = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools', 'out', 'events-' + week + '.csv')
    return event_storage

# sc will be global in IPython
sqlContext = SQLContext(sc)
#today = date.today()
today = datetime.strptime('2015-09-28', '%Y-%m-%d').date()
last_monday = today - timedelta(days=-today.weekday(), weeks=1)
week_range = pd.date_range(end=last_monday, periods=12, freq='W-MON')

# TODO for now: from events-2015-06-15.csv to events-2015-09-21.csv
WEEKS = week_range.map(lambda x: x.strftime('%Y-%m-%d'))

out_data = []
for x in range(0, len(WEEKS)):
    out_data.append([0] * len(WEEKS))

for x in range(0, len(WEEKS)):
    saved_uids = None
    saved_uids_count = None

    idx = 0
    for week in WEEKS[x:]:
        df = sqlContext.load(source='com.databricks.spark.csv', header='false', path=week_file(week))
        table_name = 'week' + week.replace('-', '_')
        df.registerTempTable(table_name)

        if not saved_uids:
            # TODO: there are no csv headers, so have to use index based columns
            signed_events = sqlContext.sql("SELECT C4 FROM " + table_name + " WHERE C5 = 'account.created'")
            new_uids = signed_events.map(lambda p: p.C4).distinct()

            saved_uids = new_uids
            saved_uids_count = int(new_uids.count())
            out_data[x][idx] = 100
        else:
            created_events = sqlContext.sql("SELECT C4 FROM " + table_name + " WHERE C5 = 'account.signed'")
            new_uids_created_events = created_events.map(lambda p: p.C4).distinct()

            retention_uids = saved_uids.intersection(new_uids_created_events)
            if saved_uids_count > 0:
                percentage = int((float(retention_uids.count()) / float(saved_uids_count)) * 100)
            else:
                percentage = 0
            out_data[x][idx] = percentage
        idx += 1

df = pd.DataFrame(out_data, index=week_range, columns=range(0, 12))

if IN_IPYTHON:
    seaborn.set(style='white')
    plt.figure(figsize=(14, 12))
    plt.title('User Retention based on "account.created" and then "account.signed"')
    seaborn.heatmap(df, annot=True, fmt='d', yticklabels=week_range, xticklabels=range(0, 12))
    # Rotate labels
    locs, labels = plt.yticks()
    plt.setp(labels, rotation=0)
    # Set axis font
    font = {
        'weight': 'bold',
        'size': 22
    }
    # Label axis
    plt.ylabel('Starting Week', **font)
    plt.xlabel('Retention Weeks', **font)
else:
    print df
