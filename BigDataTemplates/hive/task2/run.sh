#!/bin/bash

hive --hiveconf database=$1 -f udf.hql
