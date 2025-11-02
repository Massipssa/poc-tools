import os

from pyspark import SparkConf
from pyspark.sql import SparkSession

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(PACKAGE_ROOT, ".."))
WAREHOUSE_PATH = os.path.join(PROJECT_ROOT, "warehouse")


def create_spark_session(catalog_name: str, warehouse_path: str = WAREHOUSE_PATH) -> SparkSession:
    iceberg_spark_jar = 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0'

    # setup iceberg config
    conf = SparkConf() \
        .setAppName("YourAppName") \
        .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .set(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
        .set('spark.jars.packages', iceberg_spark_jar) \
        .set(f"spark.sql.catalog.{catalog_name}.warehouse", warehouse_path) \
        .set(f"spark.sql.catalog.{catalog_name}.type", "hadoop") \
        .set("spark.sql.defaultCatalog", catalog_name)

    # create spark session
    return SparkSession.builder.config(conf=conf).getOrCreate()
