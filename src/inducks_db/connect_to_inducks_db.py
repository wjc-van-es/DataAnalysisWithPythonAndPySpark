import pyspark.sql.functions as F
import os

from py4j.protocol import Py4JJavaError
from pyspark.errors import AnalysisException
from pyspark.sql import SparkSession


import project_utils.config_info as ci

ci.print_environment()
ci.check_path()

# Beware that these code examples will only work when these two environment variables are properly set
# we have set these within the Run / Debug configurations of the PyCharm IDE
postgres_password = os.environ['POSTGRES_PW']
inducks_app_password = os.environ['INDUCKS_APP_PW']
print(f"\npostgres_password: {postgres_password} and inducks_app_password={inducks_app_password}\n")

# Ingesting data from tables or views from our local postgreSQL database server
# see https://mmuratarat.github.io/2020-06-18/pyspark-postgresql-locally

# We use the jdbc driver location of our local maven repository
jdbc_driver_location = '/home/willem/.m2/repository/org/postgresql/postgresql/42.7.3/postgresql-42.7.3.jar'

spark = (SparkSession.builder
    .appName("PostgreSQL Connection with PySpark")
    .config("spark.jars", jdbc_driver_location)
    .master('local')
    .getOrCreate())

url = "jdbc:postgresql://localhost:5432/inducks_db"

properties = {
    "user": "inducks_app",
    "password": inducks_app_password,
    "driver": "org.postgresql.Driver"
}

table_name = 'pub_story_authors_summary' # The summary view of all stories in dutch publications in chronological order

try:
    # trying to see all available tables and views of the inducks_schema
    df_table_names = (spark.read.format('jdbc')
                      .option('url',url) # the same url
                      .option('driver', properties['driver']) # the same driver
                      .option('user','postgres') # we need to login as the superuser to see the table info
                      .option('password', postgres_password)
                      .option('dbtable','information_schema.tables')
                      .load()
                      .where(F.col('table_schema') == 'inducks_schema')
                      .select('table_name', 'table_type'))
    df_table_names.printSchema()
    df_table_names.show(20, truncate=False)


    df = spark.read.jdbc(url, table_name, properties=properties)
    print(f"Reading the {table_name} view from {url}, connected as user {properties['user']} "
          f"into a dataframe was successful!")
    df.printSchema()
    df.show(10, truncate=False)

    df.createOrReplaceTempView(table_name) # Dit is nog steeds nodig als we sql queries willen gebruiken.

    df_willie_wortel = spark.sql(
        f"""
        select * from {table_name}
        where protagonist_nl = 'Willie Wortel'
        """
    )
    print(df_willie_wortel.count())
    df_willie_wortel.show(287, truncate=False)

    # print view as a csv
    df.coalesce(1).write.mode("overwrite").csv("./inducks_db_pub_story_authors_summary.csv",
                                                                            sep='|', header=True, quote=None)

    # stories published in the 'Donald Duck' Weekly in 1977
    df_dd1977 = df.drop('series_code', 'series_title').where(F.col("pub_code").substr(4, 6) == "DD1977")
    print(df_dd1977.count())
    df_dd1977.show(48, truncate=False)

except Py4JJavaError as e:
    print(f"problem connecting to {url} as {properties['user']} because of {e!r}")
except AnalysisException as ae:
    print(f"{ae!r}")


if __name__ == "__main__":
    pass
