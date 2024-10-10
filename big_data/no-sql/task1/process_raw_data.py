import datetime

from pyspark.sql import functions as f
from pyspark.sql import SparkSession


with (SparkSession.builder
                  .appName('ikhlebushkin_nosql_task1')
                  .master('yarn')
                  .config('spark.sql.catalog.cassandra', 'com.datastax.spark.connector.datasource.CassandraCatalog')
                  .getOrCreate()) as spark:
    pubg_kills = spark.read.format('csv').option('header', 'true').load('/data/pubg').fillna(0)

    x_diff = pubg_kills.killer_position_x - pubg_kills.victim_position_x
    y_diff = pubg_kills.killer_position_y - pubg_kills.victim_position_y
    pubg_kills = pubg_kills.withColumn('distance', f.sqrt(f.pow(x_diff, 2) + f.pow(y_diff, 2)))

    pubg_kills = pubg_kills.withColumn('placement_diff', pubg_kills.victim_placement - pubg_kills.killer_placement)

    # write_timestamp is needed for preventing partition growing infinitely
    now = datetime.datetime.now()
    write_timestamp = f'{now.year}-{now.month}-{now.day}'

    avg_dist = pubg_kills.groupby(['killed_by', 'time']).agg(f.avg('distance').alias('distance'))
    avg_dist = avg_dist.withColumn('write_timestamp', f.lit(write_timestamp))
    (avg_dist.write.format('org.apache.spark.sql.cassandra')
                   .mode('append')
                   .options(table='dist_avg', keyspace='miptstudent2024_07')
                   .save())
    
    max_dist = pubg_kills.groupby(['killed_by', 'time']).agg(f.max('distance').alias('distance'))
    max_dist = max_dist.withColumn('write_timestamp', f.lit(write_timestamp))
    (max_dist.write.format('org.apache.spark.sql.cassandra')
                   .mode('append')
                   .options(table='dist_max', keyspace='miptstudent2024_07')
                   .save())
    
    placement_diff = pubg_kills.groupby(['killed_by', 'time']).agg(f.avg('placement_diff').alias('placement_diff'))
    placement_diff = placement_diff.withColumn('write_timestamp', f.lit(write_timestamp))
    (placement_diff.write.format('org.apache.spark.sql.cassandra')
                         .mode('append')
                         .options(table='placement_diff_avg', keyspace='miptstudent2024_07')
                         .save())
    
    old_map_kills = spark.sql('SELECT * FROM cassandra.miptstudent2024_07.map_kills_all')
    map_kills_new = pubg_kills.groupby(['map', 'killed_by', 'time']).agg(f.count('victim_name').alias('kills_count'))
    map_kills_new = map_kills_new.fillna({'map': 'unknown_map'})

    map_kills_joined = old_map_kills.withColumnRenamed('kills_count', 'kills_count_left').join(
        map_kills_new, ['killed_by', 'map', 'time'], 'outer'
    ).fillna({'kills_count_left': 0})
    map_kills_joined = map_kills_joined.fillna({'kills_count': 0})
    map_kills_joined = map_kills_joined.withColumn(
        'kills_count', map_kills_joined['kills_count_left'] + map_kills_joined['kills_count']
    ).drop('kills_count_left')
    (map_kills_joined.write
                    .format('org.apache.spark.sql.cassandra')
                    .mode('append')
                    .options(table='map_kills_all', keyspace='miptstudent2024_07')
                    .save())
