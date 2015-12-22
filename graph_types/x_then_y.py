import pandas, os, sys
# Only initialize Spark if testing locally
# Otherwise it should be already running within Spark
try:
    from pyspark import SparkContext
except ImportError:
    import dev_env

from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

IN_IPYTHON = True

try:
    __IPYTHON__
except NameError:
    IN_IPYTHON = False
    sc = SparkContext('local')
    sys.path.append(os.path.realpath(os.curdir))
    from ipynb_generators.parts.weeks import WEEKS, WEEK_RANGE, OUT_DATA, VOLUME_DATA, EVENT_STORAGE, week_file
    COHORT_QUERY = "SELECT C4 FROM %s WHERE C5 = 'account.created'"
    REST_QUERY = "SELECT C4 FROM %s"
    print "Not in IPython, creating SparkContext manually, using fake data!"

# sc will be global in IPython
sqlContext = SQLContext(sc)

for x in range(0, len(WEEKS)):
    saved_uids = None
    saved_uids_count = None

    idx = 0
    for week in WEEKS[x:]:
        df = sqlContext.load(source='com.databricks.spark.csv', header='false', path=week_file(EVENT_STORAGE, week))
        table_name = 'week' + week.replace('-', '_')
        df.registerTempTable(table_name)

        if not saved_uids:
            cohort_events = sqlContext.sql(COHORT_QUERY % table_name)
            new_uids = cohort_events.map(lambda p: p.C4).distinct()

            saved_uids = new_uids
            saved_uids_count = int(new_uids.count())
            VOLUME_DATA[x][idx] = saved_uids_count
            OUT_DATA[x][idx] = 100
        else:
            secondary_events = sqlContext.sql(REST_QUERY % table_name)
            new_uids_created_events = secondary_events.map(lambda p: p.C4).distinct()

            retention_uids = saved_uids.intersection(new_uids_created_events)
            if saved_uids_count > 0:
                percentage = int((float(retention_uids.count()) / float(saved_uids_count)) * 100)
            else:
                percentage = 0
            OUT_DATA[x][idx] = percentage
            VOLUME_DATA[x][idx] = int(retention_uids.count())
        idx += 1

DATA_FRAME = pandas.DataFrame(OUT_DATA, index=WEEK_RANGE, columns=range(0, len(WEEKS)))
VOLUME_DATA_FRAME = pandas.DataFrame(VOLUME_DATA, index=WEEK_RANGE, columns=range(0, len(WEEKS)))

if not IN_IPYTHON:
    print DATA_FRAME
    print VOLUME_DATA_FRAME
