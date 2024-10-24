from google.cloud import bigquery as bq

def create_bq_client():
    client = bq.Client(project="emiya-etl-mysql-bigq-demo")
    return client
