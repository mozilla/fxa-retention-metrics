#!/bin/bash -ex

export SPARK_HOME="${PWD}"/spark-1.3.1-bin-hadoop2.6

python tools/generate_mock_csv.py
python ipynb_generators/by_platform.py
python ipynb_generators/by_firefox_version.py
