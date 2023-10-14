from common_task import add_task
from airflow.decorators import dag
import pendulum

@dag(start_date=pendulum.datetime(2023, 10, 14, tz='UTC'))
def use_add_task():
    start = add_task.override(priority_weight=3)(1,2)
    for i in range(3):
        start >> add_task.override(task_id=f"new_add_task_{i}", retries=4)(start, i)

created_dag = use_add_task()

