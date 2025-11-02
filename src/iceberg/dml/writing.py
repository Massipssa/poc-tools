from pyspark.sql import Row

from src.iceberg.session import create_spark_session

"""
INSERT INTO allows you to insert new records into an existing Iceberg table.
"""

spark = create_spark_session("")

# Spark SQL:
spark.sql(
    "INSERT INTO glue.test.employee VALUES "
    "(1, 'Software Engineer', 'Engineering', 25000, 'NA'),"
    "(2, 'Director', 'Sales', 22000, 'EMEA')"
)

# DataFrame API:
# Create a DataFrame with the values
data = [
    Row(id=1, role='Software Engineer', department='Engineering', salary=25000, region='NA'),
    Row(id=2, role='Director', department='Sales', salary=22000, region='EMEA')
]
df = spark.createDataFrame(data)
df.writeTo("glue.test.employee").append()


# MERGE INTO is used to update an existing row based on whether a specific condition is
# met. If it is not met, you just insert the new record into the table.

spark.sql("""
    MERGE INTO glue.test.employee AS target
    USING (SELECT * FROM employee_updates) AS source
    ON target.id = source.id
    WHEN MATCHED AND source.role = 'Manager' AND source.salary > 100000 THEN
        UPDATE SET target.salary = source.salary
    WHEN NOT MATCHED THEN
        INSERT *
""")

# INSERT OVERWRITE
# To replace the data in an Iceberg table or partition with the result of a query, INSERT OVERWRITE is used.
