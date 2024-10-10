import sys

from pyspark.sql import functions as f
from pyspark.sql import SparkSession
from pyspark.sql import Window


with SparkSession.builder.appName('ikhlebushkin_spark_df_task1').master('yarn').getOrCreate() as spark:
    business = spark.read.format('json').load('/data/yelp/business').select(['business_id', 'city'])
    reviews = spark.read.format('json').load('/data/yelp/review').select(['business_id', 'stars'])

    negative_counted = (reviews
                        .where('stars < 3')
                        .groupBy('business_id')
                        .agg(f.count('stars').alias('stars_count'))).join(business,
                                                                          'business_id',
                                                                          'inner')
    
    w = Window.orderBy(negative_counted.stars_count.desc()).partitionBy('city')
    negative_tops = (negative_counted.withColumn('Rank',
                                                 f.rank().over(w))
                                     .where('Rank <= 10')
                                     .select(['business_id', 'city', 'stars_count']))
    
    negative_tops.write.mode('overwrite').csv(sys.argv[1], sep='\t')
