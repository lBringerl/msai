import json
import sys

from pyspark import SparkContext


def count_worktime(business):
    busy_dct = json.loads(business)
    _id = busy_dct['business_id']
    hours = busy_dct['hours']
    if hours is None:
        return _id, 0
    total = 0
    for v in hours.values():
        start, end = v.split('-')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        if end_m == start_m == end_h == start_h == 0:
            continue
        if end_h < start_h or (end_h == start_h and end_m < start_m):
            end_h += 24
        if end_m < start_m:
            mins = 60 - start_m + end_m
            sub_h = 1
        else:
            mins = end_m - start_m
            sub_h = 0
        total += (mins + (end_h - start_h - sub_h) * 60)
    return _id, total


with SparkContext.getOrCreate() as sc:
    businesses_rdd = sc.textFile('/data/yelp/business/yelp_academic_dataset_business.json').repartition(10)
    final_rdd = businesses_rdd.map(count_worktime).sortBy(lambda x: (-x[1], x[0]))
    final_rdd.saveAsTextFile(sys.argv[1])
    top10 = final_rdd.take(10)
    for _id, total in top10:
        print(f'{_id}\t{total}')
