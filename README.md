# fxa-retention-ipynb

## Dependencies

* Spark 1.3.1
* `com.databricks:spark-csv_2.10:1.2.0` Spark package
* Python 2.7+

## Local Setup
1. Activate `virtualenv` and install dependencies from `requirements.txt`
1. Download Spark 1.3.1:
```
wget http://apache.mirror.gtcomm.net/spark/spark-1.3.1/spark-1.3.1-bin-hadoop2.6.tgz
```
1. Set `SPARK_HOME`, example in your terminal:
```
SPARK_HOME=/Users/username/repos/fxa-retention-ipynb/spark-1.3.1-bin-hadoop2.6
```
1. Run one of the `local/` scripts to test:
```
python local/retention_events_signed.py
```

## Tools

- Generate random events:
```
python tools/generate_mock_csv.py
```
The tool above will create fake weekly exported events in `tools/out`.


## Extras

- Run Spark directly:
```
SPARK_LOCAL_IP="127.0.0.1" IPYTHON_OPTS="notebook" ./pyspark --packages com.databricks:spark-csv_2.10:1.2.0
```
After Spark loads you will be able to navigate to Spark Web UI and upload one of the `.ipynb` notebooks.
Look for `The IPython Notebook is running at` message in the terminal.

## Demo Graph
![](http://i.imgur.com/KbOZexO.jpg)

Gist Source: https://gist.github.com/vladikoff/9d2df4558299cf9c1795
