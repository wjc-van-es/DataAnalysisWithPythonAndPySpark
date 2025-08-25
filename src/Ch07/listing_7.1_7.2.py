import pyspark.sql.functions as F
import os
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
import project_utils.config_info as ci

# code that should be called before any PySpark dependencies
ci.load_env_file_when_present('project.env')

spark = SparkSession.builder.appName("Chapter 6 example").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

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


# This will throw an AnalysisException as will be printed:
# [TABLE_OR_VIEW_NOT_FOUND] The table or view `elements` cannot be found.
# Verify the spelling and correctness of the schema and catalog.
try:
    spark.sql(
        "select period, count(*) from elements "
        "where phase='liq' group by period"
    ).show(5)
except AnalysisException as e:
    print(e)

# See the next listing_7.3_7.4.py to solve the problem:
# create a temporary view "elements" from the data frame elements
# elements.createOrReplaceTempView("elements")

if __name__ == "__main__":
    pass
