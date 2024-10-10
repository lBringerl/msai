#!/bin/bash

hive --hiveconf name=$1 --hiveconf location=$2 -f create_db.hql
