from airflow.decorators import task, dag
import pendulum


@task
def add_task(x, y):
    print(f"Task args: x{x}, y={y}")
    return x + y

@dag(tags=['example'], start_date=pendulum.datetime(2023, 10, 14, tz='UTC'),)
def mydag():
    start = add_task.override(task_id="start")(1, 2)
    for i in range(3):
        start >> add_task.override(task_id=f"add_start_{i}")(start, i)

@dag(tags=['example'], start_date=pendulum.datetime(2023, 10, 14, tz='UTC'),)
def mydag2():
    start = add_task(1, 2)
    for i in range(3):
        start >> add_task.override(task_id=f"new_add_task_{i}")(start, i)

first_dag=mydag()
second_dag=mydag2()