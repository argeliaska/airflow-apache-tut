from airflow.decorators import task


# Dependency separation using Docker Operator
@task.docker(image="python:3.9-slim-bullseye",
             multiple_outputs=True)
def transform(order_data_dict: dict):
    """
    ### Tranform task
    A simple Tranform task which takes in the collection of order data and 
    computes the total order value.
    """
    total_order_value = 0

    for value in order_data_dict.values():
        total_order_value += value
    
    return {"total_order_value": total_order_value}