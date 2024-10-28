import os
from db.bigquery_connect import create_bq_client

client, bq = create_bq_client()
target_table = "emiya-etl-mysql-bigq-demo.sample_dataset.city_housing"

# The default behavior of the LoadJobConfig.write_disposition property is WRITE_APPEND
job_config = bq.LoadJobConfig(
    skip_leading_rows = 1,
    source_format = bq.SourceFormat.CSV,
    autodetect = True,
    #write_disposition = "WRITE_TRUNCATE" # Overwrite the existing data
)

cur_path = os.getcwd()
file = "city_housing.csv"
file_path = os.path.join(cur_path, "data_files", file)

with open(file_path, "rb") as source_file:
    load_job = client.load_table_from_file(
        source_file,
        target_table,
        job_config=job_config
    )

load_job.result()

destination_table = client.get_table(target_table)
print(f"There are {destination_table.num_rows} rows in the table")
