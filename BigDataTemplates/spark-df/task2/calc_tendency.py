import sys

from pyspark.sql import SparkSession
from pyspark.sql import functions as f


with SparkSession.builder.appName('ikhlebushkin_spark_df_task2').master('yarn').getOrCreate() as spark:
    business = spark.read.json('/data/yelp/business')
    checkins = spark.read.json('/data/yelp/checkin')

    categories = business.select(
        'business_id',
        f.explode(
            f.split(business.categories, ', ')
        ).alias('category')
    )
    months = checkins.select('business_id',
                            f.explode(f.split(checkins.date, ', ')).alias('checkin_date'))
    months = (months
            .withColumn('mnth', f.date_format(months.checkin_date.cast('date'), 'yyyy-MM'))
            .drop('checkin_date'))
    counted = months.groupby('business_id', 'mnth').count()
    joined_df = (categories
                 .join(counted, 'business_id', 'inner')
                 .drop('business_id')
                 .groupBy('category', 'mnth')
                 .agg(f.sum('count').alias('checkins'))
                 .orderBy('mnth', 'category')
                 .select('mnth', 'category', 'checkins'))
    joined_df.write.mode('overwrite').csv(sys.argv[1], sep='\t')
