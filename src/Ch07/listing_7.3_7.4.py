import pyspark.sql.functions as F
import os
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
import project_utils.config_info as ci

ci.print_environment()
ci.check_path()

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

table_name = 'elements'

# To be able to use a SQL query on the tabular data in data frame elements, we need to create a temporary view 
# "elements" from it
elements.createOrReplaceTempView(table_name)
print(f"After calling elements.createOrReplaceTempView('{table_name}'):\n"
      f"spark.catalog.currentCatalog() returns {spark.catalog.currentCatalog()}\n"
      f"spark.catalog.currentDatabase() returns {spark.catalog.currentDatabase()}\n"
      f"With the current database name being 'default' we want a list of its (temporary) tables with:\n"
      f"spark.catalog.listTables('default') returns:\n{spark.catalog.listTables('default')}")

try:
    spark.sql(
        f'''
        select period, count(*) 
        from {table_name} 
        where phase="liq" 
        group by period
        '''
    ).show(5)
except AnalysisException as e:
    print(e)


# print(spark.catalog.listColumns('elements', 'spark_catalog',))

# drop the temporary view when you are done.
spark.catalog.dropTempView(table_name)
print(f"List tables in catalog after calling spark.catalog.dropTempView(table_name): "
      f"{spark.catalog.listTables('default')}")
