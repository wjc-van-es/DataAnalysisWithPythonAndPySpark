from pyspark.sql import SparkSession
import pyspark.sql.functions as F

euro_sign = '\u20AC' # hex unicode codepoint literal for a euro
banknote_sign = '\u1f4b6'
frown = '\u1f612'

spark = SparkSession.builder.appName("Grocery List").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Small modification a list of tuples, works just as well as a list of lists
# we were taught that tuples are for heterogeneous data and lists for homogenous data
my_grocery_list = [
    ("Banana", 2, 1.74),
    ("Apple", 4, 2.04),
    ("Carrot", 1, 1.09),
    ("Cake", 1, 10.99),
]

df_grocery_list = spark.createDataFrame(
    my_grocery_list, ["Item", "Quantity", "Price"]
)

df_grocery_list.printSchema()
df_grocery_list.show(truncate=False)

df_total = df_grocery_list.agg(F.sum("Price").alias("total"))
df_total.show()
print(f"Our groceries have set us back {euro_sign} {df_total.first()['total']:,.2f}.")