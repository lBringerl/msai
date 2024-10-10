#!/bin/bash

export PYSPARK_PYTHON=/usr/bin/python3

spark-submit --master=yarn --num-executors=2 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4 count_backend_paths.py 2> /dev/null
