import sys

from pyspark.sql import SparkSession


_from = sys.argv[1]
to = sys.argv[2]
_map = sys.argv[3]
weapon = sys.argv[4]
s3_path = sys.argv[5]


with (SparkSession.builder
                  .appName('ikhlebushkin_nosql_task2')
                  .master('yarn')
                  .config('spark.sql.catalog.cassandra', 'com.datastax.spark.connector.datasource.CassandraCatalog')
                  .getOrCreate()) as spark:
    df = spark.sql("SELECT killed_by, map, SUM(kills_count) AS total_kills "
                   "FROM cassandra.miptstudent2024_07.map_kills_all "
                   f"WHERE killed_by = '{weapon}' AND map = '{_map}' AND time >= {_from} AND time <= {to} "
                   "GROUP BY killed_by, map")
    for row in df.collect():
        print(f'killed_by: {row.killed_by}\t|\tmap: {row.map}\t|\ttotal_kills: {row.total_kills}')
    
    spark.conf.set('fs.s3a.path.style.access', 'true')
    df.write.csv(s3_path, header=True, mode="overwrite")
