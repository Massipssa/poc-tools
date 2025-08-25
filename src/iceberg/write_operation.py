from pyspark.sql import SparkSession
from pyspark import SparkConf


if __name__ == "__main__":

    warehouse_path = "./warehouse"
    iceberg_spark_jar  = 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0'
    catalog_name = "demo"

    # setup iceberg config
    conf = SparkConf()\
        .setAppName("YourAppName") \
        .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .set(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
        .set('spark.jars.packages', iceberg_spark_jar) \
        .set(f"spark.sql.catalog.{catalog_name}.warehouse", warehouse_path) \
        .set(f"spark.sql.catalog.{catalog_name}.type", "hadoop")\
        .set("spark.sql.defaultCatalog", catalog_name) 
    
    # create spark session
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    # Create database
    spark.sql(f"CREATE DATABASE IF NOT EXISTS db")

    table_name = "db.orders"

    #########################################################################
    # Insert Query
    #########################################################################

    # 1- The engine will create warehouse/db/orders/metadata/v1.metadata.json 
    # 2- It then defines the schema of the table by specifying the columns and data types and stores it in the metadata file
    # At this point of time (snapshot in Iceberg terms) the table doesn't contains data, means there are not datafiles yet 
    # 3- The engine update the metadata pointer to point it to v1.metadata.json file in the catalog file version-hint.text
    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
        order_id BIGINT,
        customer_id BIGINT,
        order_amount DECIMAL(10, 2),
        order_ts TIMESTAMP
        ) 
        USING iceberg
        PARTITIONED BY (HOUR(order_ts))
    """)
    
    # 1- Get the location of the current metadata file
    # 2- Read schema and learn about partionning scheme to organize data accordingly while writing
    # 3- Write datafiles and related metadata files
    # 4- Engine goes to the catlog to ensure that no other snapshots were committed while this INSERT operation was being run then 
    # update the pointer to metadata file warehouse/db/orders/metadata/v2.metadata.json
    spark.sql(f"""
        INSERT INTO {table_name} VALUES (
        123,
        456,
        36.17,
        CAST('2023-03-07 08:10:23' as TIMESTAMP)
        )
    """)


    
    #########################################################################
    # Merge Query (Upsert/Merge into)
    #########################################################################

    spark.stop()