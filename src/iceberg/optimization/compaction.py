from src.iceberg.session import create_spark_session

from org.apache.iceberg import Table
from org.apache.iceberg.actions import Actions


if __name__ == '__main__':

    catalog_name = "catalog_demo"
    spark = create_spark_session(catalog_name=catalog_name)
    full_table_name = "ecommerce_db.emp_partitioned_month"

    table = spark.catalog.loadTable("glue.db.table_name")

    (
        Actions.forTable(table)
        .rewriteDataFiles()
        .binPack()  # choose bin pack strategy
        .option("target-file-size-bytes", str(512 * 1024 * 1024))  # 512 MB files
        .execute()
    )

