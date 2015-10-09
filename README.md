# fxa-retention-ipynb

[![Build Status](https://travis-ci.org/vladikoff/fxa-retention-ipynb.svg?branch=master)](https://travis-ci.org/vladikoff/fxa-retention-ipynb)

## Dependencies

* Spark 1.3.1
* `com.databricks:spark-csv_2.10:1.2.0` Spark package (included with Spark, no need to install, see `PYSPARK_SUBMIT_ARGS`)
* Python 2.7

## Local Development Setup
1. Git Clone the project and Download Spark 1.3.1 and extract it into this project directory:
```
git clone https://github.com/vladikoff/fxa-retention-ipynb.git
cd fxa-retention-ipynb
make install

```
1. Run `source ./local/bin/activate` in your terminal
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

## Commands

### `make`

Rebuild the books with changes made to files in `/ipynb_generators`.

### `make test`

Test the scripts.

### `make install`

Installs Spark and does other things to setup the project.

### `make spark`

Runs Spark locally to manually test if books in `/ipynb/dev/*` work.
After Spark loads you will be able to navigate to Spark Web UI, navigate to `/ipynb/dev` using your browser.

Open the notebook and run (>|) through all the cells to get a graph:
![](http://i.imgur.com/QhiFvd8.jpg)

### Demo Graph
![](http://i.imgur.com/KbOZexO.jpg)

Gist Source: https://gist.github.com/vladikoff/9d2df4558299cf9c1795
