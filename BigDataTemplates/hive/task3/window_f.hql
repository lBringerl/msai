ADD JAR /opt/hive/hcatalog/share/hcatalog/hive-hcatalog-core-3.1.3.jar;

USE ${hiveconf:database};

DROP TABLE IF EXISTS review;
CREATE EXTERNAL TABLE IF NOT EXISTS review
(
  review_id STRING,
  business_id STRING,
  stars FLOAT
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION '/data/yelp/review';

DROP TABLE IF EXISTS business;
CREATE EXTERNAL TABLE IF NOT EXISTS business
(
  business_id STRING,
  city STRING
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION '/data/yelp/business';

WITH counted_stars
AS(SELECT grouped_low_stars.business_id,
          business.city,
          grouped_low_stars.stars_count
FROM (SELECT business_id,
      COUNT(*) AS stars_count
      FROM (SELECT business_id,
                   stars
            FROM review
            WHERE stars < 3) AS low_stars
      GROUP BY business_id) AS grouped_low_stars
INNER JOIN business
ON grouped_low_stars.business_id=business.business_id)
SELECT business_id,
       city,
       stars_count
FROM (SELECT business_id,
              city,
              stars_count,
              ROW_NUMBER()
      OVER (PARTITION BY city
      ORDER BY stars_count DESC) AS RowNumber
      FROM counted_stars) rs WHERE RowNumber <= 10;
