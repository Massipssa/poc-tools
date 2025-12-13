from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from src.iceberg.session import create_spark_session

if __name__ == "__main__":
    catalog_name = "catalog_demo"
    spark = create_spark_session(catalog_name=catalog_name)
    spark.sparkContext.setLogLevel("ERROR")

    # Creating table using command CREATE TABLE using Spark SQL
    spark.sql(f"""
    USING iceberg
    CREATE TABLE orders (
       order_id BIGINT,
       customer_id BIGINT,
       order_amount DECIMAL(10, 2),
       order_ts TIMESTAMP
    ) 
    USING iceberg
    PARTITIONED BY (HOUR(order_ts))
    """)

    # Define the schema
    schema = StructType([
        StructField("consumer_id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("address", StringType(), True),
        StructField("email", StringType(), True)
    ])
    # Create an empty DataFrame with the schema
    df = spark.createDataFrame([], schema)
    # Write the DataFrame to the catalog as a new table
    df.writeTo("catalog_demo.ecommerce_db.consumers1").create()


    # De
    spark.sql("""
        CREATE TABLE catalog_demo.ecommerce_db.emp_partitioned (
            id INT,
            role STRING,
            department STRING)
        USING iceberg
        PARTITIONED BY (department)
    """)

    from pyspark.sql.types import StructType, StructField, StringType, IntegerType
    from pyspark.sql.functions import col

    # Define the schema
    schema = StructType([
        StructField("id", IntegerType(), True),
        StructField("role", StringType(), True),
        StructField("department", StringType(), True)
    ])
    # Create an empty DataFrame with the schema
    df = spark.createDataFrame([], schema)

    # Write the DataFrame to the catalog as a new table
    df\
        .writeTo("catalog_demo.ecommerce_db.emp_partitioned1")\
        .partitionedBy(col("department")).create()

    tab_name = "catalog_demo.ecommerce_db.emp_partitioned_month"
    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS {tab_name} (
            id INT,
            role STRING,
            department STRING,
            join_date DATE
        )
        USING iceberg
        PARTITIONED BY (days(join_date))
    """)

    # --- insert raw sample rows ---
    spark.sql(f"""
    INSERT INTO {tab_name} VALUES
      (1, 'Data Engineer',     'Platform',   DATE '2025-01-15'),
      (2, 'Analytics Engineer','BI',         DATE '2025-01-31'),
      (3, 'ML Engineer',       'ML',         DATE '2025-02-01'),
      (4, 'Data Analyst',      'Analytics',  DATE '2025-02-10'),
      (5, 'DevOps Engineer',   'Infra',      DATE '2025-02-28')
    """)

    # --- quick sanity checks ---
    spark.sql(f"""
        SELECT * 
        FROM {tab_name}
        ORDER BY join_date, id
    """).show(truncate=False)
