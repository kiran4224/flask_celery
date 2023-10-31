from celery import Celery
import os
import threading

# Configure Celery
celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

# Celery task
@celery_app.task
def my_celery_task(x, y):
    # import traceback
    # traceback.print_stack()
    # print("clelery "+ str(os.getpid()) + " " +str(threading.get_ident()))
    return x + y
