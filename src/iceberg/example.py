from src.iceberg.session import create_spark_session

if __name__ == '__main__':
    # -------------------------------------------------------------------
    # 1. Create SparkSession with Iceberg enabled (Hadoop catalog example)
    # -------------------------------------------------------------------
    catalog_name = "catalog_demo"
    spark = create_spark_session(catalog_name=catalog_name)

    # For convenience
    warehouse_path = "/tmp/iceberg_warehouse"
    table_name = "local.db_demo"  # catalog.database.table

    # -------------------------------------------------------------------
    # 2. Drop table if it exists
    # -------------------------------------------------------------------
    spark.sql(f"DROP TABLE IF EXISTS {table_name}")

    # -------------------------------------------------------------------
    # 3. Create a partitioned Iceberg table  → 1st metadata file
    # -------------------------------------------------------------------
    spark.sql(f"""
        CREATE TABLE {table_name} (
            id   INT,
            data STRING,
            ts   TIMESTAMP
        )
        USING iceberg
        PARTITIONED BY (days(ts))
        TBLPROPERTIES ('format-version' = '2')
    """)

    # Define a write sort order → written into metadata
    spark.sql(f"ALTER TABLE {table_name} WRITE ORDERED BY (ts, id)")

    # -------------------------------------------------------------------
    # 4. First commit: append some data → 2nd metadata file
    # -------------------------------------------------------------------
    df1 = spark.createDataFrame(
        [
            (1, "first batch", "2024-01-01 10:00:00"),
            (2, "first batch", "2024-01-01 12:00:00"),
            (3, "first batch", "2024-01-02 09:00:00"),
        ],
        ["id", "data", "ts"]
    ).selectExpr("id", "data", "CAST(ts AS TIMESTAMP) AS ts")

    df1.writeTo(table_name).append()

    # -------------------------------------------------------------------
    # 5. Second commit: append more data → 3rd metadata file
    # -------------------------------------------------------------------
    df2 = spark.createDataFrame(
        [
            (4, "second batch", "2024-01-02 10:00:00"),
            (5, "second batch", "2024-01-03 11:30:00"),
        ],
        ["id", "data", "ts"]
    ).selectExpr("id", "data", "CAST(ts AS TIMESTAMP) AS ts")

    df2.writeTo(table_name).append()
    spark.stop()
