import logging
import os
import sys

__name__ = "flask_celery"
log_file_path = os.path.join(sys.getcwd(), __name__)
logger_instance = None


def get_logger():
    global logger_instance
    if logger_instance :
        return logger_instance
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # logger = logging.basicConfig(filename= log_file_path, level=logging.DEBUG)
    # Create a custom logger
    logger.addHandler(logging.FileHandler(log_file_path, mode = "w"))
    logger_instance = logger
    return logger_instance

get_logger()
