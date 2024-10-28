from db.bigquery_connect import create_bq_client
from db.mysql_connect import connect_database
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# Create the BigQuery API context and client as well as the MySQL connection
client, bq = create_bq_client()
conn = connect_database()

# Variables for the BigQuery table to be created
dataset = "sample_dataset"
target_table = "annual_movie_summary_no_csv"
table_id = f"{os.getenv('GCP_PROJECT')}.{dataset}.{target_table}"

# SQL extract query
sql = """
select year, count(imdb_title_id) as movie_count, avg(duration) as avg_movie_duration,
avg(avg_vote) as avg_rating, votes from `u479841347_sql_course`.`imdb_movies` group by 1;
"""

# Extract data into a Pandas dataframe
df = pd.read_sql_query(sql, conn)

# Transform data
def year_rating(avg_rating: float) -> str:
    if avg_rating is None:
        return "no ratings"
    if avg_rating < 5.65:
        return "bad movie year"
    elif avg_rating <= 5.9:
        return "ok movie year"
    elif avg_rating <= 7:
        return "good movie year"
    else:
        return "great movie year"

# Dataframe column for average annual rating
df['year_rating'] = df['avg_rating'].apply(year_rating)

# Config for load to BigQuery
job_config = bq.LoadJobConfig(
    autodetect = True,
    write_disposition = "WRITE_TRUNCATE"
)

# Open source flat file for loading
load_job = client.load_table_from_dataframe(
    dataframe=df,
    destination=table_id,
    job_config=job_config
)

load_job.result()

destination_table = client.get_table(table_id)
print("You have {} rows in your table".format(destination_table.num_rows))
