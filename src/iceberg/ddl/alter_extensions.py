from src.iceberg.session import create_spark_session

if __name__ == '__main__':
    catalog_name = ""
    spark = create_spark_session(catalog_name=catalog_name)

    # Add partition
    spark.sql("""
        ALTER TABLE glue.test.employee ADD PARTITION FIELD region
    """)

    # Drop partition:  query  will  remove  the  partitioning  on  the  department  field  in  the
    # employee table
    spark.sql("""
        ALTER TABLE glue.test.employee DROP PARTITION FIELD department
    """)

    # Replace partition: The preceding example replaces the existing region partition field with a new parti‐
    # tion field, department, in the employee table.
    spark.sql("""
        ALTER TABLE glue.test.employee REPLACE PARTITION FIELD region WITH department
    """)