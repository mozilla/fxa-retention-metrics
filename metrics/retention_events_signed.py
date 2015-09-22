import os
from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Only initialize Spark if testing locally
# Otherwise it should be already running within Spark
if os.environ.has_key('FXA_SPARK_TESTING'):
    import spark_env

from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

try:
    __IPYTHON__
except NameError:
    sc = SparkContext('local')
    print "Not in IPython, creating SparkContext manually"


def week_file(week):
    return '../tools/out/events-' + week + '.csv'

# sc will be global in IPython
sqlContext = SQLContext(sc)
today = date.today()
last_monday = today - timedelta(days=-today.weekday(), weeks=1)
week_range = pd.date_range(end=last_monday, periods=12, freq='W-MON')

WEEKS = week_range.map(lambda x: x.strftime('%Y-%m-%d'))

out_data = []
for x in range(0, len(WEEKS)):
    out_data.append([0] * len(WEEKS))

for x in range(0, len(WEEKS)):
    saved_uids = None
    saved_uids_count = None

    idx = 0
    for week in WEEKS[x:]:
        df = sqlContext.load(source='com.databricks.spark.csv', header='true', path=week_file(week))
        table_name = 'week' + week.replace('-', '_')
        df.registerAsTable(table_name)

        signed_events = sqlContext.sql("SELECT uid FROM " + table_name + " WHERE event = 'account.signed'")

        new_uids = signed_events.map(lambda p: p.uid).distinct()

        if not saved_uids:
            saved_uids = new_uids
            saved_uids_count = int(new_uids.count())
            out_data[x][idx] = 100
        else:
            retention_uids = saved_uids.intersection(new_uids)
            if saved_uids_count > 0:
                percentage = int((float(retention_uids.count()) / float(saved_uids_count)) * 100)
            else:
                percentage = 0
            out_data[x][idx] = percentage
        idx += 1

df = pd.DataFrame(out_data, index=week_range, columns=WEEKS)
sns.set(style='white')
plt.figure(figsize=(14, 12))
plt.title('User Retention based on "account.signed"')
sns.heatmap(df, annot=True, fmt='d', yticklabels=week_range, xticklabels=range(0, 12))
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
