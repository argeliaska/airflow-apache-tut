from airflow.decorators import dag, task


# Virtualenv created dinamically for each task
@task.virtualenv(
    task_id="virtualenv_python",
    requirements=["colorama==0.4.0"],
    system_site_packages=False
)
def callable_virtualenv():
    """
    Example function that will be performed in a virtual environment.
    
    Importing at the module level ensures that it will not attempt to import the 
    library before it is installed.
    """
    from time import sleep

    from colorama import Back, Fore, Style

    print(Fore.RED + "some red text")
    print(Back.GREEN + "and with a green background")
    print(Style.DIM + "and in dim text")
    print(Style.RESET_ALL)
    for _ in range(4):
        print(Style.DIM + "Please wait...", flush=True)
        sleep(1)
    print("Finished")

virtualenv_task = callable_virtualenv()

# Python environment with pre-installed dependencies
@task.external_python(
    task_id="external_python",
    ) # python=PATH_TO_PYTHON_BINARY
def callable_external_python():
    """
    Example function that will be performed in a virtual environment.

    Importing at the module level ensures that it will not attempt to import the
    library before it is installed.
    """
    import sys
    from time import sleep

    print(f"Running task vi {sys.executable}")
    print("Sleeping")
    for _ in range(4):
        print("Please wait...", flush=True)
        sleep(1)
        print("Finished")

external_python_task = callable_external_python()

