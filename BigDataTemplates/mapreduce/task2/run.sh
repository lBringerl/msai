#!/bin/bash

OUTPUT_FOLDER=$1
TMP_FOLDER=${OUTPUT_FOLDER}-tmp

hdfs dfs -rm -r $TMP_FOLDER
yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files mapper.py,reducer.py \
    -input /data/yelp/business/ \
    -output $TMP_FOLDER \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -numReduceTasks 10

hdfs dfs -rm -r $OUTPUT_FOLDER
yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -D mapreduce.partition.keycomparator.options="-k1,1nr -k2,2" \
    -files reducer2.py \
    -input $TMP_FOLDER \
    -output $OUTPUT_FOLDER \
    -mapper cat \
    -reducer "python3 reducer2.py" \
    -numReduceTasks 1 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
