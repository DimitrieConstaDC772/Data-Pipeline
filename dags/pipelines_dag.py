from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default arguments for each DAG
default_args = {
    'start_date': datetime(2025, 7, 21),
    'retries': 1,
}

# News Pipeline DAG
with DAG(
    dag_id='news_pipeline_dag',
    default_args=default_args,
    schedule_interval='14-59/45 13-19 * * 1-5', 
    # Every 20 minutes with break 16:50 - 17:25, Mon-Fri 9am to 4pm New York Time, and 13:30 - 20:00 is New York Time in UTC
    catchup=False,
) as news_dag:

    run_news = BashOperator(
        task_id='run_news_pipeline',
        bash_command='python /opt/airflow/scripts/news_data.py', 
    )

    run_sql_com = BashOperator(
        task_id='run_sql_company_insights',
        bash_command='cd /opt/airflow/dbt_project && dbt run --select dim_company_insights.sql'
    )

    run_sql_sen = BashOperator(
        task_id='run_sql_sentiment',
        bash_command='cd /opt/airflow/dbt_project && dbt run --select fact_sentiment.sql'
    )

    # Set execution order
    run_news >> [run_sql_com, run_sql_sen]

# Share Price Pipeline DAG
with DAG(
    dag_id='share_price_pipeline_dag',
    default_args=default_args,
    schedule_interval='*/2 13-19 * * 1-5', # Every 2 minutes 
    catchup=False,
) as share_dag:

    run_share = BashOperator(
        task_id='run_share_pipeline',
        bash_command='python /opt/airflow/scripts/price_data.py', 
    )

    run_sql_price = BashOperator(
        task_id='run_sql_price',
        bash_command='cd /opt/airflow/dbt_project && dbt run --select fact_share_price.sql'
    )

    # Set execution order
    run_share >> run_sql_price

    # Change time logic for python scrypts and bring all the logic here because you included the sql in the dags.