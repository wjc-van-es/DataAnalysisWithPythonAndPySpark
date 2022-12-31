"""Checkpoint code for the book Data Analysis with Python and PySpark, Chapter 4."""

import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DIRECTORY = "../../data/broadcast_logs"
logs = (
    spark.read.csv(
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

log_identifier = spark.read.csv(
    os.path.join(DIRECTORY, "ReferenceTables/LogIdentifier.csv"),
    sep="|",
    header=True,
    inferSchema=True,
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

full_log.show(20, truncate=False)
