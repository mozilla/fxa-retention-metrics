#!/bin/bash -ex

export SPARK_HOME="${PWD}"/spark-1.3.1-bin-hadoop2.6

python tools/generate_mock_csv.py
python tests/test_convert_to_book.py
python ipynb_generators/created_then_anything_by_platform.py
python ipynb_generators/created_then_anything_by_firefox_version.py
python ipynb_generators/signed_then_anything.py
python graph_types/x_then_y.py
