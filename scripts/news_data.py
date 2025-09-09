
# Import Libraries
import requests
import pandas as pd
import os
from google.cloud import bigquery
from datetime import datetime, timedelta, timezone
import time
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F


# Extract news data with GNews API


# Use MY_ENV_PATH to hide location of key
env_path = os.getenv("MY_ENV_PATH")
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("GNEWS_API_KEY")
topics = ['"Amazon" OR "Jeff Bezos" OR "Andy Jassy" OR "AWS"', 
          '"Tesla" OR "Elon Musk" OR "Cybertruck" OR "FSD" OR Gigafactory', 
          '"Nvidia" OR "NVIDIA GPUs" OR "Jensen Huang" OR "CUDA" OR "RTX"', 
          '"Meta Platforms" OR "Facebook" OR "Instagram" OR "WhatsApp" OR "Mark Zuckerberg"',
          '"Microsoft Corp." OR "Microsoft" OR "Windows" OR "Xbox" OR "Satya Nadella" OR "Azure"']

# Point to the service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_ENV")
# Initialise client
client = bigquery.Client()

# Get last batch upload time
query = """
SELECT MAX(batch_upload_time) AS last_upload
FROM `bq-client-462019.fin_pipeline_data.News_DF`
"""
last_batch_upload = list(client.query(query).result())[0].last_upload

now_utc = datetime.now(timezone.utc)

# Determine if we should skip the 45-minute logic
skip_recent_cutoff = False
if last_batch_upload and (now_utc.date() > last_batch_upload.date()):
    skip_recent_cutoff = True

# 45-minute cutoff
recent_cutoff = now_utc - timedelta(minutes=45)

results = []

for topic in topics:
    url = f'https://gnews.io/api/v4/search?q={topic}&token={api_key}&lang=en&max=10'

    response = requests.get(url)
    data = response.json()

    article_number = 0

    for article_data in data.get('articles', []):
        try:
            published_str = article_data.get('publishedAt')
            published_dt = datetime.fromisoformat(published_str.replace("Z", "+00:00"))
            # extract only the name from topics
            first_term = topic.split(' OR ')[0].strip('"')
            
                # Include article if we skip recent cutoff (new day) OR it's within last 45 mins
            if skip_recent_cutoff or published_dt > recent_cutoff:
                # Append the data to results
                results.append({
                    'Company': first_term,
                    'Title': article_data.get('title'),
                    'Time': published_dt,
                    'Source': article_data.get('source', {}).get('name'),
                    'URL': article_data.get('url'),
                    'Content': article_data.get('content')
                })
                article_number += 1
                if article_number >= 3:
                    break                               # Limit the data to 3 articles per topic
                time.sleep(1)
        except ValueError:
            print("Invalid datetime format in publishedAt.")

# Create DataFrame
news_df = pd.DataFrame(results)




# Sentiment Analysis




# Load tokeniser and model from Hugging Face 
tokenizer = AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")

# Label news based on sentiment (positive, neutral, negative) using FinBERT

# Write a function that will label every summary from the news DataTable
sentiment = []
if not news_df.empty:
    for _, row in news_df[['Company', 'Content']].iterrows(): # Make sure this does not run if news_df is empty
        article = row['Content']
        company = row['Company']
        inputs = tokenizer(article, return_tensors="pt", truncation=True, max_length=512)
        outputs = model(**inputs)
        # Get probabilities
        probs = F.softmax(outputs.logits, dim=1)
        # Map labels (neutral, positive, negative)
        labels = ['neutral', 'positive', 'negative']
        # Get highest probability label
        pred_label = labels[probs.argmax()]
        pred_prob = probs.max().item()
        sentiment.append({
            "Company": company,
            "Label": pred_label,
            "Probability": pred_prob
        })
else:
    print("There are no fresh news. Skipping sentiment analysis.")
# Create DataFrame
sentiment_df = pd.DataFrame(sentiment)



# Upload DataFrames to fin_pipeline_data dataset in BigQuery



# Drop the Content Column from the news_df for storage efficiency
if not news_df.empty:
    news_df = news_df.drop(columns=['Content'])
else:
    print("There are no fresh news. Skipping sentiment analysis.")

# List the DataFrames
dfs = [news_df, sentiment_df]
table_names = ["News_DF", "Sentiment_DF"]

# Loop through the list of DataFrames and upload the information to the fin_pipeline_data dataset
for df, name in zip (dfs, table_names):
    table_id = f"bq-client-462019.fin_pipeline_data.{name}"
    df['batch_upload_time'] = datetime.now(timezone.utc)
    job = client.load_table_from_dataframe(df, table_id)
    job.result()
    print(f"Loaded {job.output_rows} rows to {table_id}")