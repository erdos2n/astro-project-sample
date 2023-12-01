import logging

from datetime import datetime

from airflow.decorators import task, dag

@task
def hello_world():
	logging.info("hello world...")
	logging.info("goodbye world...")


@dag(
	dag_id="hello_airflow",
	schedule=None,
	start_date=datetime(2023, 12, 1),
)
def my_dag():
	return hello_world()


my_dag()

