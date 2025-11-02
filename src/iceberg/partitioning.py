from pyspark import SparkConf
from pyspark.sql import SparkSession

if __name__ == "__main__":

    warehouse_path = "./warehouse"
    iceberg_spark_jar = 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0'
    catalog_name = "demo"

    # setup iceberg config
    """
    - catalog name 
    - catalog type
    - warehouse
    """

    conf = SparkConf() \
        .setAppName("YourAppName") \
        .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .set(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
        .set('spark.jars.packages', iceberg_spark_jar) \
        .set(f"spark.sql.catalog.{catalog_name}.warehouse", warehouse_path) \
        .set(f"spark.sql.catalog.{catalog_name}.type", "hadoop") \
        .set("spark.sql.defaultCatalog", catalog_name)

    # create spark session
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    table_name = "db.persons"

    # Partition evolution
    spark.sql(f"""ALTER TABLE {table_name} ADD PARTITION FIELD truncate(name, 2)""")
