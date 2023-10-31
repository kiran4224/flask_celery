# Flask Celery APP

celery run command 
    "celery -A celery_task worker -l INFO"

flask run command 
    gunicorn --bind 0.0.0.0:5000 -w 2 flask_app:app
