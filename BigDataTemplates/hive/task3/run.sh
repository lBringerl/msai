#!/bin/bash

hive --hiveconf database=$1 -f window_f.hql
