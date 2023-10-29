import pyspark.sql.functions as F
import os
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException

# To prevent the warning:
# WARN package: Truncated the string representation of a plan since it was too large. This behavior can be adjusted by
# setting 'spark.sql.debug.maxToStringFields'.
# You can safely ignore it, if you are not interested in seeing the sql schema logs. Otherwise, you might want to set
# the property to a higher value, but it might affect the performance of your job:
# the default of spark.sql.debug.maxToStringFields is 25
spark = (SparkSession.builder
         .appName("Chapter 7 example")
         .master("local") # running locally https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.builder.master.html#pyspark.sql.SparkSession.builder.master
         .config('spark.sql.debug.maxToStringFields', '50')
         .getOrCreate())

spark.sparkContext.setLogLevel("WARN")

spark.conf.set('spark.debug.maxToStringFields', '100')
# spark.conf.
data_dir = "../../data/elements"

elements = (spark
            .read
            .csv(
                os.path.join(data_dir, "Periodic_Table_Of_Elements.csv"),
                header=True,
                inferSchema=True,
            ))

elements.printSchema()
elements.where(F.col("phase") == "liq").groupby("period").count().show()

# To be able to use a SQL query on the tabular data in data frame elements, we need to create a temporary view 
# "elements" from it
elements.createOrReplaceTempView('elements')
print(f"After calling elements.createOrReplaceTempView('elements'):\n"
      f"spark.catalog.currentDatabase(): {spark.catalog.currentDatabase()}\n"
      f"spark.catalog.listTables('default'): {spark.catalog.listTables('default')}")

try:
    spark.sql(
        '''
        select period, count(*) 
        from elements 
        where phase="liq" 
        group by period
        '''
    ).show(5)
except AnalysisException as e:
    print(e)
print(spark.catalog.currentDatabase())
print(spark.catalog.listTables('default'))

# print(spark.catalog.listColumns('elements', 'None',))

# drop the temporary view when you are done.
spark.catalog.dropTempView("elements")
print(f"List tables in catalog after calling spark.catalog.dropTempView('elements'): "
      f"{spark.catalog.listTables('default')}")
