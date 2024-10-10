#!/bin/bash

OUTPUT_FOLDER=$1

hdfs dfs -rm -r $OUTPUT_FOLDER

yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D stream.num.map.output.key.fields=1 \
    -D mapreduce.partition.keypartitioner.options=-k2,2 \
    -files mapper.py,reducer.py \
    -input /data/yelp/review_sample,/data/yelp/user_sample \
    -output $OUTPUT_FOLDER \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -numReduceTasks 8 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
