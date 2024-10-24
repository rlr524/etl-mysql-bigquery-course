from db.bigquery_connect import create_bq_client

client = create_bq_client()

sql = "select * from sample_dataset.movies_ratings limit 100"

query_job = client.query(sql)

results = query_job.result()

for r in results:
    print(f"{r.year} | {r.title} | {r.genre} | {r.movie_rating}")
