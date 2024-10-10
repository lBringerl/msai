ADD JAR /opt/hive/hcatalog/share/hcatalog/hive-hcatalog-core-3.1.3.jar;
ADD FILE mapper.py;

USE ${hiveconf:database};

DROP TABLE IF EXISTS business;

CREATE EXTERNAL TABLE IF NOT EXISTS business
(
    attributes MAP<STRING, STRING>
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION '/data/yelp/business';

SELECT TRANSFORM(attributes)
USING 'python3 mapper.py' AS (keys STRING, counter INT)
FROM business
WHERE attributes IS NOT NULL
ORDER BY keys
