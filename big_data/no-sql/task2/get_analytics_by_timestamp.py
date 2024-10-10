import sys

from pyspark.sql import SparkSession


_from = sys.argv[1]
to = sys.argv[2]
weapon = sys.argv[3]
timestamp = sys.argv[4]
s3_path = sys.argv[5]


with (SparkSession.builder
                  .appName('ikhlebushkin_nosql_task2')
                  .master('yarn')
                  .config('spark.sql.catalog.cassandra', 'com.datastax.spark.connector.datasource.CassandraCatalog')
                  .getOrCreate()) as spark:
    dist_avg = spark.sql(
        "SELECT * FROM cassandra.miptstudent2024_07.dist_avg "
        f"WHERE write_timestamp = '{timestamp}' AND killed_by = '{weapon}' AND time >= {_from} AND time <= {to}"
    ).withColumnRenamed('distance', 'distance_avg')
    dist_max = spark.sql(
        "SELECT * FROM cassandra.miptstudent2024_07.dist_max "
        f"WHERE write_timestamp = '{timestamp}' AND killed_by = '{weapon}' AND time >= {_from} AND time <= {to}"
    ).withColumnRenamed('distance', 'distance_max')
    placement_diff = spark.sql(
        "SELECT * FROM cassandra.miptstudent2024_07.placement_diff_avg "
        f"WHERE write_timestamp = '{timestamp}' AND killed_by = '{weapon}' AND time >= {_from} AND time <= {to}"
    )
    joined_df = dist_avg.join(dist_max, on=['write_timestamp', 'killed_by', 'time'])
    joined_df = joined_df.join(placement_diff, on=['write_timestamp', 'killed_by', 'time'])
    for row in joined_df.collect():
        print(f'timestamp: {row.write_timestamp}\t|\tweapon: {row.killed_by}\t|\t'
            f'time: {row.time}\t|\tdistance_avg: {row.distance_avg}\t|\t'
            f'distance_max: {row.distance_max}\t|\tplacement_diff: {row.placement_diff}')
        
    spark.conf.set('fs.s3a.path.style.access', 'true')
    joined_df.write.csv(s3_path, header=True, mode="overwrite")
