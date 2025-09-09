WITH latest_news AS (
  SELECT *
  FROM `bq-client-462019.fin_pipeline_data.News_DF`
  WHERE batch_upload_time = (
    SELECT MAX(batch_upload_time)
    FROM `bq-client-462019.fin_pipeline_data.News_DF`
  )
),
latest_sentiment AS (
  SELECT *
  FROM `bq-client-462019.fin_pipeline_data.Sentiment_DF`
  WHERE batch_upload_time = (
    SELECT MAX(batch_upload_time)
    FROM `bq-client-462019.fin_pipeline_data.Sentiment_DF`
  )
)
SELECT
    sen.Company,
    sen.Label,
    CAST(sen.Probability AS FLOAT64) AS Probability,
    CAST(news.Time AS TIMESTAMP) AS TimeN
FROM latest_sentiment sen
JOIN latest_news news
  ON sen.Company = news.Company
ORDER BY TimeN
