ADD JAR /opt/hive/hcatalog/share/hcatalog/hive-hcatalog-core-3.1.3.jar;
ADD FILE mapper.py;

USE ${hiveconf:database};

DROP TABLE IF EXISTS business;

CREATE EXTERNAL TABLE IF NOT EXISTS business
(
  business_id STRING,
  is_open INTEGER,
  hours STRUCT <Monday: STRING,
                Tuesday: STRING,
                Wednesday: STRING,
                Thursday: STRING,
                Friday: STRING,
                Saturday: STRING,
                Sunday: STRING>
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION '/data/yelp/business';

FROM business
SELECT TRANSFORM(
    business_id,
    is_open,
    hours.Monday,
    hours.Tuesday,
    hours.Wednesday,
    hours.Thursday,
    hours.Friday,
    hours.Saturday,
    hours.Sunday
) USING 'python3 mapper.py' AS (
    id STRING,
    total STRING
);
