import pyspark.sql.functions as f
from pyspark.sql.types import StringType, StructType, StructField, TimestampType
from pyspark.sql import SparkSession


@f.udf
def split_path(path):
    if path[-1] == '/' and len(path) != 1:
        path = path[:-1]
    paths = [path]
    left, *_ = path.rsplit('/', 1)
    while len(left) > 0:
        paths.append(left)
        left, *_ = left.rsplit('/', 1)
    return ' '.join(paths)


@f.udf
def get_path(message):
    _, path = message.rsplit(' ', 1)
    return path


schema = StructType([
    StructField("time", TimestampType()),
    StructField("message", StringType())
])


with SparkSession.builder.appName('ikhlebushkin_task2_backend').master('yarn').getOrCreate() as spark:
    df = (spark
          .readStream
          .format("kafka")
          .option("kafka.bootstrap.servers", "master.hadoop.akhcheck.ru:9092")
          .option("subscribe", "student07-backend")
          .load())
    dstream = df.selectExpr("topic", "CAST(key AS STRING)", "CAST(value AS STRING)")
    dstream = dstream.withColumn('json', f.from_json(f.col('value'), schema))
    dstream = dstream.withColumn('time', f.col('json.time').alias('time'))
    dstream = dstream.withColumn('message', f.col('json.message').alias('message'))
    dstream = dstream.filter(dstream.message.contains('[DEBUG]'))
    dstream = dstream.withColumn('path', get_path(dstream.message).alias('path'))
    dstream = dstream.withColumn('paths', f.explode(f.split(split_path(dstream.path), ' ')))
    aggregated_dstream = (dstream
                          .withWatermark("time", "24 hours")
                          .groupBy(f.window(dstream.time, "1 minutes", "1 minutes"), "paths")
                          .count())

    query = (aggregated_dstream
            .writeStream
            .outputMode("complete")
            .format("console")
            .option("truncate", "false")
            .start())
    query.awaitTermination()
