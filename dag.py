from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args={
    "owner":"airflow",
    "depends_on_past":False,
    "email_on_failure":False,
    "retries":1,
    "retry_delay":timedelta(minutes=1),
    }
dag=DAG("weather_api_dag",default_args=default_args,
        description="a simple ETl dag",
        schedule_interval=timedelta(minutes=5),
        start_date=datetime(2024,10,29),
        catchup=False,)
etl_run=BashOperator(
    task_id='run_etl',
    bash_command='bash /home/mani/wrapper.sh ',
    dag=dag,
)