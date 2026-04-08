# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %md 
# MAGIC #which vendor make the most revenue?

# COMMAND ----------

df = spark.read.table("nyctaxi.02_silver.yellow_trips_enriched")
from pyspark.sql.functions import sum, round, desc
df.groupBy("vendor")\
   .agg(round(sum("total_amount"), 2).alias("total_revenue"))\
   .orderBy("total_revenue", ascending=False).display()


# COMMAND ----------

# MAGIC %md
# MAGIC #which is the most pick up borough?

# COMMAND ----------

df.\
    groupBy("pu_borough").\
        agg(
            count("*").alias("number_of_trips")).\
            orderBy("number_of_trips", ascending=False).\
                display()
        

# COMMAND ----------

# MAGIC %md 
# MAGIC #which is the most commom journey(borough to borough)?

# COMMAND ----------

df.groupBy(concat("pu_borough",lit("-->"),"do_borough").alias("journey")).\
    agg(count("*").alias("number_of_trips")).\
        orderBy("number_of_trips", ascending=False).\
            display()

# COMMAND ----------

# MAGIC %md
# MAGIC #create a time series showing  the number of trips and total revenue per day?
# MAGIC

# COMMAND ----------

df2 = spark.read.table("nyctaxi.03_gold.daily_trip_summary")

# COMMAND ----------

df2.display()

# COMMAND ----------

