import os
from google.cloud import bigquery as bq
from dotenv import load_dotenv

load_dotenv()

def create_bq_client():
    """
    :return: A tuple consisting of an instantiation of a BigQuery Client (client)
    and the Google BigQuery API wrapper itself (bq).
    """
    project = os.getenv("GCP_PROJECT")
    client = bq.Client(project=project)
    return client, bq
