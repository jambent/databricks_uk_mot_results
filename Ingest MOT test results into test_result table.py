# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM personaldatabricks.uk_mot_results.test_result LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS personaldatabricks.uk_mot_results.test_result;
# MAGIC CREATE TABLE personaldatabricks.uk_mot_results.test_result;

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO personaldatabricks.uk_mot_results.test_result
# MAGIC FROM '/Volumes/personaldatabricks/uk_mot_results/uk_mot_data_volume/test_result_20220531131730_32355.csv'
# MAGIC   FILEFORMAT = CSV
# MAGIC   FORMAT_OPTIONS ('mergeSchema' = 'true',
# MAGIC                   'delimiter' = ',',
# MAGIC                   'header' = 'true')
# MAGIC   COPY_OPTIONS ('mergeSchema' = 'true');

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM personaldatabricks.uk_mot_results.test_result LIMIT 10;
