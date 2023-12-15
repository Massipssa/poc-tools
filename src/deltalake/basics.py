import pyspark
from pyspark.sql.functions import *
from delta import *


if __name__ == '__main__':

    tmp_path = "/tmp1/delta-table"

    builder = pyspark.sql\
        .SparkSession\
        .builder.appName("MyApp") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    data = spark.range(0, 5)

    # create table
    data.write.format("delta").save(tmp_path)

    # load data
    df = spark.read.format("delta").load(tmp_path)
    df.show()

    # overwrite
    data = spark.range(5, 10)
    data.write.format("delta").mode("overwrite").save(tmp_path)

    deltaTable = DeltaTable.forPath(spark, tmp_path)

    # Update every even value by adding 100 to it
    deltaTable.update(
        condition=expr("id % 2 == 0"),
        set={"id": expr("id + 100")})

    # Delete every even value
    deltaTable.delete(condition=expr("id % 2 == 0"))

    # Upsert (merge) new data
    newData = spark.range(0, 20)

    deltaTable.alias("oldData") \
        .merge(
        newData.alias("newData"),
        "oldData.id = newData.id") \
        .whenMatchedUpdate(set={"id": col("newData.id")}) \
        .whenNotMatchedInsert(values={"id": col("newData.id")}) \
        .execute()

    deltaTable.toDF().show()
