#!/bin/bash

# from, to, weapon, timestamp, s3_path

export AWS_ACCESS_KEY_ID=miptstudent2024-07
export AWS_SECRET_ACCESS_KEY=miptstudent2024-07
export AWS_ENDPOINT_URL=http://master.hadoop.akhcheck.ru:9000
export CQLSH_HOST=master.hadoop.akhcheck.ru

spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.12:3.2.0,org.apache.hadoop:hadoop-aws:3.2.2 \
             --conf spark.sql.extensions=com.datastax.spark.connector.CassandraSparkExtensions \
             --conf spark.cassandra.connection.host=$CQLSH_HOST \
             --conf spark.hadoop.fs.s3a.aws.credentials.provider=org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider \
             --conf spark.hadoop.fs.s3a.access.key=$AWS_ACCESS_KEY_ID \
             --conf spark.hadoop.fs.s3a.secret.key=$AWS_SECRET_ACCESS_KEY \
             --conf spark.hadoop.fs.s3a.endpoint=$AWS_ENDPOINT_URL \
             --conf spark.hadoop.fs.s3a.signing-algorithm=S3SignerType get_analytics_by_timestamp.py $1 $2 $3 $4 $5

# execution example
# ./reader_basic_stats.sh 10 1000 AKM 2024-5-29 "s3a://miptstudent2024-07/pubg/basic_stats.csv"
