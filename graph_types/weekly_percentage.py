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
    TOTAL_QUERY = "SELECT C4 FROM %s WHERE C5 = 'account.created'"
    CHUNK_QUERIES = [
        ("Android", TOTAL_QUERY + " AND C3 = 'Android'"),
        ("Firefox for iOS", TOTAL_QUERY + " AND C1 = 'FxiOS'")
    ]
    print "Not in IPython, creating SparkContext manually, using fake data!"

# sc will be global in IPython
sqlContext = SQLContext(sc)

WEEKLY_DATA = {}


for week in WEEKS:
    df = sqlContext.load(source='com.databricks.spark.csv', header='false', path=week_file(EVENT_STORAGE, week))
    table_name = 'week' + week.replace('-', '_')
    df.registerTempTable(table_name)

    total_events = sqlContext.sql(TOTAL_QUERY % table_name)
    total_mapped_events = total_events.map(lambda p: p.C4)
    total_count = total_mapped_events.count()

    for query in CHUNK_QUERIES:
        chunk_name = query[0]
        sql_query = query[1]

        chunk_events = sqlContext.sql(sql_query % table_name)
        chunk_mapped_events = chunk_events.map(lambda p: p.C4)
        chunk_count = chunk_mapped_events.count()

        if chunk_mapped_events > 0:
            percentage = int((float(chunk_count) / float(total_count)) * 100)
        else:
            percentage = 0

        WEEKLY_DATA.setdefault(chunk_name, []).append(percentage)

print WEEKLY_DATA