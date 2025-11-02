from src.iceberg.session import create_spark_session

if __name__ == "__main__":
    catalog_name = "catalog_demo"
    table_name = "catalog_demo.ecommerce_db.emp_partitioned_month"
    spark = create_spark_session(catalog_name=catalog_name)

    spark.sql(f"DROP TABLE {table_name}")

    spark.sql(f"DROP TABLE {table_name} PURGE")
