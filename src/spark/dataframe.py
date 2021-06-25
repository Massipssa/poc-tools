from src.spark.context import spark
from pyspark.sql import DataFrame
from pyspark.sql.functions import max, desc


def read_csv(path):
    return spark\
        .read\
        .option("inferSchema", "true")\
        .option("header", "true")\
        .csv(path)


def explain_df(path):

    sorted_df = read_csv(path)\
        .sort("count")

    sorted_df.explain()
    sorted_df.show(10)


def df_sql(df: DataFrame):
    df.createOrReplaceTempView("data_2015")
    max_1 = spark.sql("""select max(count) from data_2015""")
    max_2 = df.select(max("count"))


def top_five_destinations(df: DataFrame):
    df.groupby("DEST_COUNTRY_NAME")\
        .sum("count")\
        .withColumnRenamed("sum(count)", "destination_total")\
        .orderBy(desc("destination_total"))\
        .limit(5)\
        .show()
