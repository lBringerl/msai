import json
import sys

from operator import add
from pyspark import SparkContext


def fetch_user_id_useful(review_line):
    dct_review = json.loads(review_line)
    return dct_review['user_id'], dct_review['useful']


def fetch_user_id_friends(user_line):
    dct_user = json.loads(user_line)
    return [(friend, dct_user['user_id']) for friend in dct_user['friends'].strip().split(', ')]


def fetch_user_id_friends_number(user_line):
    dct_user = json.loads(user_line)
    friends_list = dct_user['friends'].strip().split(', ')
    if friends_list[0] == 'None':
        friends_number = 0
    else:
        friends_number = len(friends_list)
    return dct_user['user_id'], friends_number


def sorting_criteria(merge_line):
    usefuls, influence = merge_line[1]
    influence = 0 if influence is None else influence
    return usefuls * influence


with SparkContext.getOrCreate() as sc:
    reviews = sc.textFile('/data/yelp/review_sample').repartition(10)
    users = sc.textFile('/data/yelp/user_sample').repartition(10)

    reviews_rdd0 = reviews.map(lambda x: fetch_user_id_useful(x))
    reviews_rdd1 = reviews_rdd0.groupByKey().mapValues(list)
    reviews_rdd2 = reviews_rdd1.map(lambda x: (x[0], sum(sorted(x[1], reverse=True)[:5])))

    users_rdd0 = users.flatMap(lambda x: fetch_user_id_friends(x))
    users_rdd1 = users.map(lambda x: fetch_user_id_friends_number(x))
    users_rdd2 = users_rdd1.leftOuterJoin(users_rdd0).map(lambda x: (x[1][1], x[1][0])).reduceByKey(add)

    merge_rdd = reviews_rdd2.leftOuterJoin(users_rdd2).sortBy(lambda x: sorting_criteria(x), ascending=False)
    merge_rdd.saveAsTextFile(sys.argv[1])

    top10 = merge_rdd.take(10)
    for influencer in top10:
        _id, (usefuls, influence) = influencer
        print(f'{_id}\t{usefuls}\t{influence}')
