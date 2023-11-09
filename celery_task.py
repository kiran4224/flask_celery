from celery import Celery, shared_task,Task
import os
import threading
import time
from redis_test import test


# Configure Celery
celery_app = Celery(
    'tasks',
    broker='redis://apm_redis:6379/0',
    backend='redis://apm_redis:6379/0'
)


# Celery task
@celery_app.task
def my_celery_task(x, y):
    # import traceback
    # traceback.print_stack()
    print("clelery "+ str(os.getpid()) + " " +str(threading.get_ident()))
    time.sleep(0.01*x*y)
    test()
    return x + y

@shared_task
def print_app_name():
    current_app_name = print_app_name.app
    print(f"The current Celery application name is: {current_app_name.main}")

# class MyTaskClass(Task):
#     name = "MyTaskClasses"
#     def run(self, x, y):
#         return x + y

# celery_app.tasks.register(MyTaskClass())


# def my_task(x, y):
#     return x + y

# celery_app.task(name='my_task')(my_task)


def call_tasks(x,y):
    result = my_celery_task.delay(x, y)
    # MyTaskClass.delay(x, y)
    # my_task.delay(x,y)
    print_app_name.delay()
    return result
