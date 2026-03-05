from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("validation").getOrCreate()

df = spark.read.csv("sample_data/members_sample.csv", header=True)

print("Total rows:", df.count())

df.groupBy("dues").count().show()