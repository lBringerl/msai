import pyspark.sql.functions as f
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import SparkSession


with SparkSession.builder.appName('ikhlebushkin_stream_splitter').master('yarn').getOrCreate() as spark:
    df = (spark
          .readStream
          .format("kafka")
          .option("kafka.bootstrap.servers", "master.hadoop.akhcheck.ru:9092")
          .option("subscribe", "test")
          .load())
    dstream = df.selectExpr("topic", "CAST(key AS STRING)", "CAST(value AS STRING)")
    schema = StructType([StructField("method", StringType()), StructField("kubernetes", StringType())])
    kubernetes_schema = StructType([StructField("labels", StringType())])
    labels_schema = StructType([StructField("app", StringType())])
    dstream = dstream.withColumn('topic', f.lit('empty'))
    dstream = dstream.withColumn('json', f.from_json(f.col('value'), schema))
    dstream = dstream.withColumn('kubernetes', f.from_json(f.col('json.kubernetes'), kubernetes_schema))
    dstream = dstream.withColumn('labels', f.from_json(f.col('kubernetes.labels'), labels_schema))
    dstream = dstream.withColumn('app', f.col('labels.app').alias('app'))
    dstream = dstream.withColumn('topic', f.when(dstream.app == 'frontend', 'student07-frontend').otherwise(dstream.topic))
    dstream = dstream.withColumn('topic', f.when(dstream.app == 'backend', 'student07-backend').otherwise(dstream.topic))
    dstream = dstream.withColumn('topic', f.when(dstream.app == 'webservice', 'student07-gitlab').otherwise(dstream.topic))
    ds = (dstream
        .writeStream
        .format("kafka")
        .option("kafka.bootstrap.servers", "master.hadoop.akhcheck.ru:9092")
        .option("checkpointLocation", "checkpoints-test")
        .start()
        .awaitTermination())
