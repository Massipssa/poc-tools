import sys
import argparse
import re
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from pyspark.sql import types as T
from datetime import datetime, timedelta

"""
--warehouse: s3://<HERE>/iceberg/
--db: testDb
--table: testTable
--input: s3://<HERE>/test/
"""
# ----------------------------
# Parse Glue job args
# ----------------------------
# Glue passes JOB_NAME via getResolvedOptions; for custom args we can also use argparse
glue_args = getResolvedOptions(sys.argv, ["JOB_NAME"])
parser = argparse.ArgumentParser()
parser.add_argument("--warehouse", required=True, help="S3 warehouse path, e.g. s3://bucket/warehouse")
parser.add_argument("--db", required=True, help="Iceberg database/namespace name")
parser.add_argument("--table", required=True, help="Iceberg table name")
parser.add_argument("--input", required=False, help="Optional CSV source")
args, _ = parser.parse_known_args()


warehouse = args.warehouse.rstrip("/")
raw_db, raw_tbl = args.db, args.table
db = re.sub(r'[^a-z0-9_]', '_', raw_db.lower())
table = re.sub(r'[^a-z0-9_]', '_', raw_tbl.lower())
if db != raw_db or table != raw_tbl:
    print(f"Normalized identifiers: db='{raw_db}' → '{db}', table='{raw_tbl}' → '{table}'")
full_table = f"{db}.{table}"
print(f"Table name: {full_table}")

# --------------------------------------------------------
# Iceberg GlueCatalog configuration
# --------------------------------------------------------

conf = SparkConf() \
  .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
  .set("spark.sql.defaultCatalog", "glue") \
  .set("spark.sql.catalog.glue", "org.apache.iceberg.spark.SparkCatalog") \
  .set("spark.sql.catalog.glue.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog") \
  .set("spark.sql.catalog.glue.warehouse", warehouse) \
  .set("spark.sql.catalog.glue.io-impl", "org.apache.iceberg.aws.s3.S3FileIO") \
  .set("spark.sql.catalog.glue.write.format-version", "2")

# --------------------------------------------------------
# Spark / Glue context
# --------------------------------------------------------
sc = SparkContext.getOrCreate(conf=conf)   # creates session with the static configs
glue_ctx = GlueContext(sc)
spark = glue_ctx.spark_session 
job = Job(glue_ctx)
job.init(glue_args["JOB_NAME"], {})

# --------------------------------------------------------
# Create namespace (database) if not exists
# --------------------------------------------------------
spark.sql(f"CREATE NAMESPACE IF NOT EXISTS glue.{db}")

# --------------------------------------------------------
# Create a DataFrame (CSV or synthetic)
# --------------------------------------------------------
schema = T.StructType([
    T.StructField("id", T.IntegerType(), False),
    T.StructField("name", T.StringType(), True),
    T.StructField("email", T.StringType(), True),
    T.StructField("country", T.StringType(), True),
    T.StructField("signup_ts", T.TimestampType(), True),
])

if args.input:
    df = (
        spark.read
        .option("header", True)
        .schema(schema)
        .csv(args.input)
        .withColumn("signup_ts", F.coalesce(F.col("signup_ts"), F.current_timestamp()))
    )
else:
    # Small synthetic dataset
    now = datetime.utcnow()
    data = [
        (1, "Alice", "alice@example.com", "FR", now),
        (2, "Bob",   "bob@example.com",   "DE", now),
        (3, "Cara",  "cara@example.com",  "US", now),
    ]
    df = spark.createDataFrame(data, schema=schema)

# --------------------------------------------------------
# Create table (if not exists) and write initial data
# --------------------------------------------------------
# Create with properties (format v2) and a partitioning example
spark.sql(f"""
CREATE TABLE IF NOT EXISTS glue.{full_table} (
    id INT,
    name STRING,
    email STRING,
    country STRING,
    signup_ts TIMESTAMP
)
USING ICEBERG
PARTITIONED BY (country) -- example partitioning
TBLPROPERTIES (
  'format-version' = '2'
)
""")

# Overwrite or append initial data
# If the table is empty, overwrite is fine; for idempotency you can use overwriteDynamicPartitions if you prefer
(df
    .writeTo(f"glue.{full_table}")
    .overwritePartitions()
)

print(f"Inserted initial data into glue.{full_table}")

# --------------------------------------------------------
# Upsert using MERGE INTO
# --------------------------------------------------------
updates_data = [
    # Update id=2 (Bob -> Robert), insert new id=4
    (2, "Robert", "bob@example.com", "DE", datetime.utcnow() + timedelta(minutes=5)),
    (4, "Dina",   "dina@example.com", "FR", datetime.utcnow() + timedelta(minutes=5)),
]
updates_df = spark.createDataFrame(updates_data, schema=schema)
updates_df.createOrReplaceTempView("updates_src")

spark.sql(f"""
MERGE INTO glue.{full_table} t
USING updates_src s
ON t.id = s.id
WHEN MATCHED THEN UPDATE SET
  t.name      = s.name,
  t.email     = s.email,
  t.country   = s.country,
  t.signup_ts = s.signup_ts
WHEN NOT MATCHED THEN INSERT *
""")

print("Merge completed")

# --------------------------------------------------------
# Query current table
# --------------------------------------------------------
print("Current snapshot:")
spark.sql(f"SELECT * FROM glue.{full_table} ORDER BY id").show(truncate=False)

# --------------------------------------------------------
# Time travel example (as-of-timestamp)
# --------------------------------------------------------
# Get a timestamp ~2 minutes ago to read the previous version (adjust as needed)
as_of = int((datetime.utcnow() - timedelta(minutes=2)).timestamp() * 1000)

historical = (
    spark.read
    .format("iceberg")
    .option("as-of-timestamp", as_of)
    .load(f"glue.{full_table}")
)
print("Historical read (as-of ~2 minutes ago):")
historical.orderBy("id").show(truncate=False)

job.commit()
