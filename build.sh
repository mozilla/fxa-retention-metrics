#!/bin/bash -ex

export SPARK_HOME="${PWD}"/spark-1.3.1-bin-hadoop2.6

python tools/generate_mock_csv.py
python ipynb_generators/created_then_anything_by_platform.py
python ipynb_generators/created_then_anything_by_firefox_version.py
python ipynb_generators/created_then_anything_by_service.py
python ipynb_generators/signed_then_anything.py
python ipynb_generators/multi_device.py
python ipynb_generators/weekly_created_percentage.py
python ipynb_generators/weekly_login_percentage.py
python ipynb_generators/weekly_created_percentage_by_service.py
python ipynb_generators/weekly_login_percentage_by_service.py
