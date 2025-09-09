WITH latest_prices AS (
  SELECT *
  FROM `bq-client-462019.fin_pipeline_data.Prices_DF`
  WHERE batch_upload_time = (
    SELECT MAX(batch_upload_time)
    FROM `bq-client-462019.fin_pipeline_data.Prices_DF`
  )
)
SELECT
    Company,
    CAST(Time AS TIMESTAMP) AS TimeN,
    CAST(Price as FLOAT64) AS Price
FROM latest_prices
ORDER BY TimeN