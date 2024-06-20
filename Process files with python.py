# Databricks notebook source
import os

for root,dirs,files in os.walk('/Volumes/personaldatabricks/uk_mot_results/uk_mot_data_volume/'):
    for file in files: 
        print(f'{file}')

# COMMAND ----------

pip install databricks-sql-connector

# COMMAND ----------

# MAGIC %pip install --upgrade pip

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %pip install python-dotenv

# COMMAND ----------

from databricks import sql
import os
from dotenv import load_dotenv

load_dotenv()

with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       = os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token=   os.getenv("DATABRICKS_ACCESS_TOKEN")) as connection:
    
    with connection.cursor() as cursor:
        for root,dirs,files in os.walk('/Volumes/personaldatabricks/uk_mot_results/uk_mot_data_volume/'):
            for file in files:
                cursor.execute(f'''COPY INTO personaldatabricks.uk_mot_results.test_result
                FROM '/Volumes/personaldatabricks/uk_mot_results/uk_mot_data_volume/{file}'
                FILEFORMAT = CSV
                FORMAT_OPTIONS ('mergeSchema' = 'true',
                  'delimiter' = ',',
                  'header' = 'true')
                COPY_OPTIONS ('mergeSchema' = 'true');''')

