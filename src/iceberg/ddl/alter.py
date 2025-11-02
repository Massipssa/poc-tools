"""
As time of writing the operations are only supported using Spark SQL
"""
from src.iceberg.session import create_spark_session

if __name__ == '__main__':
    catalog_name = ""
    table_name = ""
    new_table_name = ""

    spark = create_spark_session(catalog_name=catalog_name)

    # Rename column -> doesn't change the storage path, just the namespace in the catalog
    spark.sql(f"""
        ALTER TABLE {table_name} RENAME TO {new_table_name}
    """)

    # Set table property
    spark.sql(f"""
        ALTER TABLE {table_name} SET TBLPROPERTIES ('write.wap.enabled'='true')
    """)

    # Add column
    # 1: add one column
    spark.sql("""
        ALTER TABLE glue.test.employee ADD COLUMN manager STRING
    """)
    # 2: add multiple columns: you can add multiple column at same time
    spark.sql("""
        ALTER TABLE glue.test.employee ADD COLUMN details STRING, manager_id INT
    """)
    # 3: add column at specific position: done using the FIRST and AFTER clauses
    spark.sql("""
    ALTER TABLE glue.test.employee ADD COLUMN new_column bigint AFTER department
    """)

    spark.sql("""
    ALTER TABLE glue.test.employee ADD COLUMN first_column bigint FIRST
    """)

    # Renaming a column: In this query, we altered the employee table within the glue.test catalog by renam‐
    # ing role to title to better reflect the relevant column name.
    spark.sql("""
        ALTER TABLE glue.test.employee RENAME COLUMN role TO title
    """)

    # Modifying a column: only safe updates are allowed
    spark.sql("""
        ALTER TABLE glue.test.employee ALTER COLUMN id TYPE BIGINT
    """)

    # Drop column
    spark.sql("""
        ALTER TABLE glue.test.employee DROP COLUMN department
    """)