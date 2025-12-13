from src.iceberg.session import create_spark_session

if __name__ == '__main__':
    catalog_name = "catalog_demo"
    spark = create_spark_session(catalog_name=catalog_name)
    full_table_name = "ecommerce_db.emp_partitioned_month"
    #
    # spark.sql(f"""
    #   CALL {catalog_name}.system.rewrite_manifests(
    #     table => '{full_table_name}'
    #   )
    # """)

    print("Rewrite manifests")
    # spark.sql(f"CALL {catalog_name}.system.rewrite_manifests('{full_table_name}')")

    # to avoid OOM with spark
    spark.sql(f"CALL {catalog_name}.system.rewrite_manifests('{full_table_name}', false)")

    print("Remove orphan files")
    spark.sql(f"""
      CALL {catalog_name}.system.remove_orphan_files(
        table => '{full_table_name}',
        dry_run => true
      )
    """)
