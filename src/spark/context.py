from pyspark import SparkConf
from pyspark.sql import SparkSession

# spark.sql.shuffle.partitions: is set to 200 by default

conf = SparkConf()\
    .setAppName("test-app")\
    .set("spark.sql.shuffle.partitions", 5)\
    .setMaster('local[*]')\


spark = SparkSession \
    .builder \
    .config(conf=conf) \
    .getOrCreate()

sc = spark.sparkContext
