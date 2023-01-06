"""Checkpoint code for the book Data Analysis with Python and PySpark, Chapter 4."""

import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DIRECTORY = "../../data/broadcast_logs"
logs = (spark
    .read
    .option('encoding', 'IBM860')
    .csv(
        os.path.join(DIRECTORY, "BroadcastLogs_2018_Q3_M8_sample.CSV"),
        sep="|",
        header=True,
        inferSchema=True,
        timestampFormat="yyyy-MM-dd",
    )
    .drop("BroadcastLogID", "SequenceNO")
    .withColumn(
        "duration_seconds",
        (
                F.col("Duration").substr(1, 2).cast("int") * 60 * 60
                + F.col("Duration").substr(4, 2).cast("int") * 60
                + F.col("Duration").substr(7, 2).cast("int")
        ),
    )
)

log_identifier = (spark
    .read
    .option('encoding', 'IBM860')
    .csv(
        os.path.join(DIRECTORY, "ReferenceTables/LogIdentifier.csv"),
        sep="|",
        header=True,
        inferSchema=True,
    )
)

cd_category = spark.read.csv(
    os.path.join(DIRECTORY, "ReferenceTables/CD_Category.csv"),
    sep="|",
    header=True,
    inferSchema=True,
).select(
    "CategoryID",
    "CategoryCD",
    F.col("EnglishDescription").alias("Category_Description"),
)

cd_program_class = spark.read.csv(
    os.path.join(DIRECTORY, "ReferenceTables/CD_ProgramClass.csv"),
    sep="|",
    header=True,
    inferSchema=True,
).select(
    "ProgramClassID",
    "ProgramClassCD",
    F.col("EnglishDescription").alias("ProgramClass_Description"),
)

logs_and_channels = logs.join(log_identifier, on='LogServiceID', how='inner')

full_log = (logs_and_channels
            .join(cd_category, on='CategoryID', how='left')
            .join(cd_program_class, on='ProgramClassID', how='left')
            )

full_log.printSchema()

# we can have multiple aggregation functions as arguments to the agg() method, which become separate columns
# that we can give a customized name with the alias() method
# here we embellished listing 5.11 with a 'mean duration' as second aggregation column
commercials = ['COM', 'PRC', 'PGI', 'PRO', 'LOC', 'SPO', 'MER', 'SOL']

answer = (
    full_log.groupby("LogIdentifierID")
    .agg(
        F.sum(
            F.when(
                F.trim(F.col('ProgramClassCD')).isin(commercials),
                F.col('duration_seconds')
            ).otherwise(0)
        ).alias('duration_commercial'),
        F.sum("duration_seconds").alias("duration_total"),
    )
    .withColumn(
        "commercial_ratio", F.col(
            'duration_commercial') / F.col('duration_total')
    )
    .orderBy('commercial_ratio', ascending=False)
)

answer.printSchema()
print(f"total number of records in answer data frame is  {answer.count()}")
answer.show(1000, truncate=False)

call_signs = (spark
    .read
    .option('encoding', 'UTF-8')
    .csv(
        os.path.join(DIRECTORY, "Call_Signs.csv"),
        sep=",",
        header=True,
        inferSchema=True,
    ).drop('UndertakingNO')
)

call_signs.printSchema()
call_signs.show(truncate=False)

answer_plus = (answer.join(call_signs, on='LogIdentifierID', how='left_outer')
    .select('LogIdentifierID', 'Undertaking_Name', 'commercial_ratio')
    .orderBy('commercial_ratio', ascending=False)
    .fillna('')
    .fillna(0)
 )

answer_plus.printSchema()
print(f"total number of records in answer_plus data frame is  {answer_plus.count()}")
answer_plus.show(1000, truncate=False)