#!/usr/bin/env python

import sys
import pyspark.sql.functions as F
import os
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
import project_utils.config_info as ci

# We have to add the src dir to the sys.path to be able to import the project_utils module
# when run from the command line
from pathlib import Path
src_dir = Path(__file__).parents[1]
print(src_dir)
# sys.path.append(src_dir)
# sys.path.append(src_dir / 'project_utils')

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
         .master("local[*]")
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

elements.createOrReplaceTempView("elements")

print('elements ordered by Era, Year, AtomicNumber')
try:
    df_pt_in_order_of_discovery =  spark.sql(
        '''
        select 
            AtomicNumber, 
            Symbol,
            Element, 
            Period, 
            Group, 
            Type,
            Discoverer,
            Year,
            -- https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-case.html
            case Discoverer 
                when 'Prehistoric' then 1 
                when 'Early historic times' then 2 
                else 3 
            end as Era
        from elements 
        order by Era, Year, AtomicNumber
        '''
    )
    df_pt_in_order_of_discovery.show(10, truncate=False)
    df_pt_in_order_of_discovery.coalesce(1).write.mode("overwrite").csv("./elements_in_order_of_discovery.csv",
                                                                        sep='|', header=True, quote=None)
except AnalysisException as e:
    print(e)

print('elements ordered by Group NULLS LAST, AtomicNumber')
try:
    df_pt_in_order_of_group= spark.sql(
        '''
        select 
            AtomicNumber,
            Symbol, 
            Element, 
            Period, 
            Group, 
            Type,
            NumberofValence,
            NumberofShells
        from elements 
        order by              
            Group NULLS LAST, --https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-orderby.html
            AtomicNumber
        '''
    )
    df_pt_in_order_of_group.show(20, truncate=False)
    df_pt_in_order_of_group.coalesce(1).write.mode("overwrite").csv("./elements_in_order_of_group.csv",
                                                                        sep='|', header=True, quote=None)
except AnalysisException as e:
    print(e)
# print(spark.catalog.listColumns('elements', 'None',))
print(f"spark.catalog.currentDatabase(): "
      f"{spark.catalog.currentDatabase()}")
print(f"List tables in catalog before calling spark.catalog.dropTempView('elements'): "
      f"{spark.catalog.listTables('default')}")
spark.catalog.dropTempView("elements")
print(f"List tables in catalog after calling spark.catalog.dropTempView('elements'): "
      f"{spark.catalog.listTables('default')}")

if __name__ == "__main__":
    pass
