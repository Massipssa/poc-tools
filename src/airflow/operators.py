from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'massi',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 26),
    'email': ['massipssa.kerrache@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


@dag(default_args)
def simple_etl():
    mysql_task = MySqlOperator(
        task_id="create_table_mysql",
        sql="/scripts/sql/create_mysql_table.sql",
        mysql_conn_id="mysql_cnx"
    )
    postgres_table = PostgresOperator(
        task_id="create_table_postgres",
        sql="/scripts/sql/create_postgres_table.sql",
        mysql_conn_id="postgres_cnx"
    )
    mysql_task >> postgres_table


@task(task_id="run_this")
def run_this_func(dag_run=None):
    print(f"Remotely received value of {dag_run.conf.get('message')} for key=message")


with DAG(
        dag_id="example_trigger_target_dag",
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        schedule=None,
        tags=["example"],
) as dag:
    run_this = run_this_func()

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Here is the message: $message"',
        env={"message": '{{ dag_run.conf.get("message") }}'},
    )
