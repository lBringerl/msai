#!/bin/bash

spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.12:3.2.0 \
             --conf spark.sql.extensions=com.datastax.spark.connector.CassandraSparkExtensions \
             --conf spark.cassandra.connection.host=master.hadoop.akhcheck.ru process_raw_data.py
