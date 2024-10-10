import pyspark.sql.functions as f
from pyspark.sql.types import StringType, StructType, StructField, TimestampType
from pyspark.sql import SparkSession


schema = StructType([
    StructField("time", TimestampType()),
    StructField("code", StringType())
])


with SparkSession.builder.appName('ikhlebushkin_task2_frontend_codes').master('yarn').getOrCreate() as spark:
    df = (spark
          .readStream
          .format("kafka")
          .option("kafka.bootstrap.servers", "master.hadoop.akhcheck.ru:9092")
          .option("subscribe", "student07-frontend")
          .load())
    dstream = df.selectExpr("topic", "CAST(key AS STRING)", "CAST(value AS STRING)")
    dstream = dstream.withColumn('json', f.from_json(f.col('value'), schema))
    dstream = dstream.withColumn('time', f.col('json.time').alias('time'))
    dstream = dstream.withColumn('code', f.col('json.code').alias('code'))
    aggregated_dstream = (dstream
                          .withWatermark("time", "24 hours")
                          .groupBy(f.window(dstream.time, "1 minutes", "1 minutes"), "code")
                          .count())
    
    query = (aggregated_dstream
             .writeStream
             .outputMode("complete")
             .format("console")
             .option("truncate", "false")
             .start())
    query.awaitTermination()
