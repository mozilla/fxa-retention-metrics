import os
import sys

# Read more at http://renien.github.io/blog/accessing-pyspark-pycharm/
# Append pyspark to Python Path
sys.path.append(os.path.join(os.environ['SPARK_HOME'], 'python'))
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.databricks:spark-csv_2.10:1.2.0'
os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'

try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print ("Successfully imported Spark Modules")

except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)
