# Data-Pipeline
Sentiment Analysis Data Pipeline

## 1. Data Collection: Financial News
Tool: Python (requests, BeautifulSoup, or NewsAPI)

Goal: Collect news headlines and article snippets related to selected stock tickers (e.g., AAPL, TSLA, AMZN).
## 2. Sentiment Analysis
Tool: FinBERT (for finance-specific sentiment) or VADER (for simplicity)

Goal: Assign a numeric sentiment score to each article headline.
## 3. SQL Database (Staging + Production Tables)
Tool: PostgreSQL or BigQuery

Goal: Store raw + cleaned data using SQL for further querying and aggregation.

SQL Tables:
news_raw → stores raw scraped articles

sentiment_scores → stores processed scores

daily_summary → aggregated sentiment per ticker per day

## 4. Data Modeling with DBT (Optional but Impressive)
Tool: DBT

Goal: Model SQL transformations like:

Daily average sentiment

Tickers with largest sentiment swings

Sector-level rollups

## 5. Automation (Airflow or DBT Scheduler)
Tool: Apache Airflow (or DBT Cloud Scheduler)

Goal: Automate daily pipeline:

Run Python scripts → sentiment scoring

Load into SQL → run DBT models

Refresh Power BI dashboard

## 6. Data Visualization
Tool: Power BI

Goal: Build an interactive dashboard with:

📈 Sentiment trend per stock

🔔 “High volatility” or “Negative press” alerts

📊 Sector comparison (average sentiment by sector)

🧠 “Analyst Notes” section (human interpretation box)
