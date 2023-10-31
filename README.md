# Flask Celery APP

celery run command 

        "celery -A celery_task worker -l INFO"

flask run command 

        gunicorn --bind 0.0.0.0:5000 -w 2 flask_app:app

Api Request

        curl -X POST -H "Content-Type: application/json" -d '{"x": 4, "y": 6}' http://localhost:5000/add
