#!/bin/bash

OUTPUT_FOLDER=$1

hdfs dfs -rm -r $OUTPUT_FOLDER

yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files mapper.py,reducer.py \
    -input /data/yelp/business/ \
    -output $OUTPUT_FOLDER \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -numReduceTasks 1
