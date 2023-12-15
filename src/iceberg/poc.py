from pyspark.sql import SparkSession
from pyspark import SparkConf

if __name__ == "__main__":


    # setup iceberg config
    conf = SparkConf().setAppName("YourAppName") \
        .set("spark.jars.packages", "org.apache.hadoop.fs.s3a.S3AFileSystem:3.3.1") \
        .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .set("spark.sql.catalog.demo", "org.apache.iceberg.spark.SparkCatalog")\
        .set("spark.sql.catalog.demo.io-impl", "org.apache.iceberg.aws.s3.S3FileIO") \
        .set("spark.sql.catalog.demo.warehouse", "s3a://openlake/warehouse/") \
        .set("spark.sql.catalog.demo.s3.endpoint", "https://play.min.io:50000") \
        .set("spark.sql.defaultCatalog", "demo") \
        .set("spark.sql.catalogImplementation", "in-memory") \
        .set("spark.sql.catalog.demo.type", "hadoop") \
        .set("spark.executor.heartbeatInterval", "300000") \
        .set("spark.network.timeout", "400000")
    """
    import pyspark
    conf = (
        pyspark.SparkConf()
        .setAppName('app_name')
        # packages
        #.set('spark.jars.packages', 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12-1.4.2 iceberg-spark-runtime-3.3_2.12:1.1.0')
        # SQL Extensions
        .set('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions')
        # Configuring Catalog
        #.set('spark.sql.catalog.spark_catalog', 'org.apache.iceberg.spark.SparkCatalog')
        #.set('spark.sql.catalog.spark_catalog.warehouse', './warehouse')
        #.set('spark.sql.catalog.spark_catalog.type', 'hadoop')
    )
    """

    # create spark session
    spark = SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()

    # create a dataframe
    data = [("John", 28, "Doctor"), ("Bob", 35, "Singer"), ("Charlie", 42, "Teacher")]
    columns = ["name", "age", "job_title"]
    df = spark.createDataFrame(data, columns)

    table_path = "./data/iceberg"
    df.write \
        .format("iceberg") \
        .mode("overwrite") \
        .save("table_path")

    iceberg_df = spark.read.format("iceberg").load("table_path")
    iceberg_df.show()
