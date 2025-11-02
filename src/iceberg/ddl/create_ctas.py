from src.iceberg.session import create_spark_session

"""
When running CTAS in the context of Apache Iceberg is that it works as an atomic operation only when using the
 SparkCatalog class. If you use the SparkSessionCatalog class, CTAS is supported but is not atomic, which may cause 
 inconsistencies when concurrent writes are occurring
"""

if __name__ == "__main__":
    catalog_name = "catalog_demo"
    spark = create_spark_session(catalog_name=catalog_name)
    spark.sparkContext.setLogLevel("ERROR")

    spark.sql("""
        CREATE TABLE glue.test.employee_ctas
        USING iceberg
        AS SELECT * FROM glue.test.sample
    """)

    # Read an existing table into a DataFrame
    df_ctas = spark.read.table("glue.test.sample")

    # Use the DataFrame's writeTo method with the create operation to do a CTAS
    df_ctas.writeTo("glue.test.employee_ctas").create()
