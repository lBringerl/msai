#!/bin/bash

# from, to, map, weapon, s3_path

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
             --conf spark.hadoop.fs.s3a.signing-algorithm=S3SignerType get_map_analytics.py $1 $2 $3 $4 $5

# execution example
# ./reader_map_kills.sh 10 2000 ERANGEL 'AKM' "s3a://miptstudent2024-07/pubg/map_kills.csv"
