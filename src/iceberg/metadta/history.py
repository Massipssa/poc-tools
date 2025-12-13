from src.iceberg.session import create_spark_session

if __name__ == '__main__':
    catalog_name = "catalog_demo"
    spark = create_spark_session(catalog_name=catalog_name)
    full_table_name = "local.db_demo"

    tables = [
        "history",
        "metadata_log_entries",
        "snapshots",
        "files",
        "manifests",
        "partitions",
        "all_data_files",
        "all_manifests",
        "refs",
        "entries"
    ]

    for i, t in enumerate(tables, start=1):
        print(f"{i} - {t} table")
        spark.sql(f"SELECT * FROM {full_table_name}.{t}").show(truncate=False)

    # small_files = f"""
    #    SELECT
    #        partition,
    #        COUNT(*) AS num_files,
    #        AVG(file_size_in_bytes) AS avg_file_size
    #    FROM
    #        {files_table}
    #    GROUP BY
    #        partition
    #    ORDER BY
    #        num_files DESC,
    #        avg_file_size ASC
    #    """
    # spark.sql(f"{small_files}").show()
    #
    # check_null_values = f"""
    #    SELECT
    #        partition,
    #        file_path
    #    FROM
    #        {files_table}
    #    WHERE
    #        null_value_counts['3'] > 0
    #    """
    # spark.sql(f"{check_null_values}").show()
    #
    # print("Sum of data file")
    # spark.sql(f"SELECT sum(file_size_in_bytes) from {files_table}").show()
    #
    # print("File in snapshot")
    # spark.sql(f"SELECT file_path, file_size_in_bytes FROM {files_table} VERSION AS OF 1223704394949634677").show()