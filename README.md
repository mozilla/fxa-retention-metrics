# fxa-retention-ipynb

[![Build Status](https://travis-ci.org/vladikoff/fxa-retention-ipynb.svg?branch=master)](https://travis-ci.org/vladikoff/fxa-retention-ipynb)

## Dependencies

* Spark 1.3.1
* `com.databricks:spark-csv_2.10:1.2.0` Spark package (included with Spark, no need to install, see `PYSPARK_SUBMIT_ARGS`)
* Python 2.7

## Local Development Setup
1. Setup `virtualenv` by running `make build`
1. Run `source ./local/bin/activate` in your terminal
1. Download Spark 1.3.1 and extract it into this project directory:
```
wget http://apache.mirror.gtcomm.net/spark/spark-1.3.1/spark-1.3.1-bin-hadoop2.6.tgz
```
1. Set `SPARK_HOME`, example in your terminal:
```
export SPARK_HOME=<project_directory>/spark-1.3.1-bin-hadoop2.6
```
1. Run the csv script to generate random data:
```
python tools/generate_mock_csv.py
```
1. Run one of the `metrics/` scripts to test the graphs on sample data:
```
python metrics/retention_events_signed.py
```
1. Work on new metrics scripts in `/metrics`, once ready create a new conversion script under `/books` for your new metrics script.
1. Run the conversion script, e.g `python books/retention_events_signed.py`
1. Upload your new `.ipynb` to a local Spark UI for testing or [telemetry-dash.mozilla.org](http://telemetry-dash.mozilla.org/)

## Extras

### Run Spark locally:
```
SPARK_LOCAL_IP="127.0.0.1" IPYTHON_OPTS="notebook" ./pyspark --packages com.databricks:spark-csv_2.10:1.2.0
```
After Spark loads you will be able to navigate to Spark Web UI, click 'Upload' and select one of the `.ipynb` notebooks in `/ipynb/dev`.

Open the notebook and run (>|) through all the cells to get a graph:
![](http://i.imgur.com/QhiFvd8.jpg)

### Demo Graph
![](http://i.imgur.com/KbOZexO.jpg)

Gist Source: https://gist.github.com/vladikoff/9d2df4558299cf9c1795
