iceberg_spark_jar = 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0'

# Set Iceberg Jar
conf = SparkConf() \
    .setAppName("YourAppName") \
    .set('spark.jars.packages', iceberg_spark_jar) \

# Create spark session
spark = SparkSession.builder.config(conf=conf).getOrCreate()

warehouse_path = "./warehouse"
iceberg_spark_jar = 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0'
catalog_name = "demo"

# Setup iceberg config
conf = SparkConf() \
    .setAppName("YourAppName") \
    .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .set(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
    .set('spark.jars.packages', iceberg_spark_jar) \
    .set(f"spark.sql.catalog.{catalog_name}.warehouse", warehouse_path) \
    .set(f"spark.sql.catalog.{catalog_name}.type", "hadoop") \
    .set("spark.sql.defaultCatalog", catalog_name)

# Create spark session
spark = SparkSession.builder.config(conf=conf).getOrCreate()