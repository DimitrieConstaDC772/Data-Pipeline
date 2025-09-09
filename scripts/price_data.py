
# Import libraries:
import requests
import pandas as pd
import os
from google.cloud import bigquery
from datetime import datetime, time, timezone
from dotenv import load_dotenv


# Extract share prices from Finnhub


# Use MY_ENV_PATH to hide location of key
env_path = os.getenv("MY_ENV_PATH")
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("FINNHUB_API_KEY")
assets = {"AMZN": "Amazon", "TSLA": "Tesla", "NVDA": "Nvidia", "META": "Meta Platforms", "MSFT": "Microsoft Corp."}
latest_prices = []

for ticker, name in assets.items():
    url = f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}'
    response = requests.get(url).json()
    price = response['c']
    timestamp = response['t']
    time = pd.to_datetime(timestamp, unit='s', utc=True)
    latest_prices.append({
        'Company': name,
        'Price': price,
        'Time': time
    })
# Create DataFrame
prices_df = pd.DataFrame(latest_prices)



# Upload DataFrames to fin_pipeline_data dataset in BigQuery



# Point to the service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_ENV")

# Initialise client
client = bigquery.Client()
# List the DataFrames
dfs = [prices_df]
table_names = ["Prices_DF"]

# Loop through the list of DataFrames and upload the information to the fin_pipeline_data dataset
for df, name in zip (dfs, table_names):
    table_id = f"bq-client-462019.fin_pipeline_data.{name}"
    df['batch_upload_time'] = datetime.now(timezone.utc)
    job = client.load_table_from_dataframe(df, table_id)
    job.result()
    print(f"Loaded {job.output_rows} rows to {table_id}")