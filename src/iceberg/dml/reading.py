from src.iceberg.session import create_spark_session

spark = create_spark_session("")

# Read all
spark.sql("SELECT * FROM glue.test.employee").show()

df_emp = spark.table("glue.test.employee")

# Filter
# Spark SQL
spark.sql("SELECT * FROM glue.test.employee WHERE department = 'Marketing'").show()

# Dataframe API
df_emp = spark.table("glue.test.employee")
filtered_df = df_emp.filter(df_emp['department'] == 'Marketing')
filtered_df.show()

## Aggregations

## Count
# Spark SQL:
spark.sql("SELECT COUNT(*) FROM glue.test.employee").show()

# DataFrame API:
df_emp = spark.table("glue.test.employee")
print(df_emp.count())

## AVG
## Spark SQL:
spark.sql("SELECT AVG(salary) FROM glue.test.employee").show()

##  DataFrame API:
df_emp = spark.table("glue.test.employee")
df_emp.agg({'salary': 'avg'}).show()
