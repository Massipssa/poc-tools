from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


if __name__ == "__main__":

    warehouse_path = "./warehouse"
    iceberg_spark_jar  = 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0'
    catalog_name = "demo"

    # setup iceberg config
    conf = SparkConf().setAppName("YourAppName") \
        .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .set(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
        .set('spark.jars.packages', iceberg_spark_jar) \
        .set(f"spark.sql.catalog.{catalog_name}.warehouse", warehouse_path) \
        .set(f"spark.sql.catalog.{catalog_name}.type", "hadoop")\
        .set("spark.sql.defaultCatalog", catalog_name) 
    
    # create spark session
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    # create a dataframe
    schema = StructType([
        StructField('name', StringType(), True),
        StructField('age', IntegerType(), True),
        StructField('job_title', StringType(), True)
    ])

    data = [("person1", 28, "Doctor"), ("person2", 35, "Singer"), ("person3", 42, "Teacher")]
    df = spark.createDataFrame(data, schema=schema)
    
    # Create database
    spark.sql(f"CREATE DATABASE IF NOT EXISTS db")
    
    # write and read Iceberg table
    table_name = "db.persons"
    df.write.format("iceberg").mode("overwrite").saveAsTable(f"{table_name}")
    iceberg_df = spark.read.format("iceberg").load(f"{table_name}")
    iceberg_df.printSchema()
    iceberg_df.show()
  
    # Schema evolution
    spark.sql(f"ALTER TABLE {table_name} RENAME COLUMN job_title TO job")
    spark.sql(f"ALTER TABLE {table_name} ALTER COLUMN age TYPE bigint")
    spark.sql(f"ALTER TABLE {table_name} ADD COLUMN salary FLOAT AFTER job")
    iceberg_df = spark.read.format("iceberg").load(f"{table_name}")
    iceberg_df.printSchema()
    iceberg_df.show()

    spark.sql(f"SELECT * FROM {table_name}.snapshots").show()


    # ACID
    spark.sql(f"UPDATE {table_name} SET salary = 100")
    spark.sql(f"DELETE FROM {table_name} WHERE age = 42")
    spark.sql(f"INSERT INTO {table_name} values ('Charlie', 50, 'Teacher', 2000)")
    spark.sql(f"SELECT * FROM {table_name}.snapshots").show()

    # Partitioning the table
    spark.sql(f"ALTER TABLE {table_name} ADD PARTITION FIELD age")
    spark.read.format("iceberg").load(f"{table_name}").where("age = 28").show()
    

    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS {table_name}
        (name STRING, age INT, job STRING, salary INT)
        USING iceberg
        PARTITIONED BY (age)
        """
    )
    
    # Time travel 
    spark.sql(f"SELECT * FROM {table_name}.snapshots").show(2, truncate=False)
    spark.read.option("snapshot-id", "2133194735081165190").table(table_name).show()
    spark.read.option("as-of-timestamp", "2133194735081165190").table(table_name).show()
