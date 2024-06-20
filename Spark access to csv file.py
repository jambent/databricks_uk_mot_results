# Databricks notebook source
from pyspark.sql import SparkSession

spark = (SparkSession
 .builder
 .appName("SparkReadCSVExample")
 .getOrCreate())

csv_file = "/Volumes/personaldatabricks/uk_mot_results/uk_mot_data_volume/test_result_20220531131730_32361.csv"

df = (spark.read.format("csv")
 .option("inferSchema", "true")
 .option("header", "true")
 .load(csv_file))
df.createOrReplaceTempView("2021_partial_test_result")

spark.sql("""SELECT test_date, test_mileage, test_result 
FROM 2021_partial_test_result 
WHERE 
first_use_date between '2009-01-01' AND '2009-12-31'
AND make = 'FORD' AND model = 'FOCUS'
AND colour = 'BLUE' AND fuel_type = 'PE'
ORDER BY test_mileage DESC""").show(30)


# COMMAND ----------

#Equivalent DataFrame treatment
from pyspark.sql.functions import col, desc

(df.select("test_date", "test_mileage", "test_result")
 .where(col("first_use_date") >= '2009-01-01')
 .where(col("first_use_date") <= '2009-12-01')
 .where(col("make") == 'FORD')
 .where(col("model") == 'FOCUS')
 .where(col("colour") == 'BLUE')
 .where(col("fuel_type") == 'PE')
 .orderBy(desc("test_mileage"))).show(30)
