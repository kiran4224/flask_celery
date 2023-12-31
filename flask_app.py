from flask import Flask, request, jsonify
from celery_task import celery_app, call_tasks
import os
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to flask application"

@app.route('/add', methods=['POST'])
def add_numbers():
    print("flask " + str(os.getpid()) +" "+ str(threading.get_ident()))
    try:
        if request.method == 'POST':
            x = int(request.form['x'])
            y = int(request.form['y'])
            result = call_tasks(x,y)
            # result = my_celery_task.delay(x, y)
            # worker_hostname = result.backend.get_task_meta(result.id)
            # print(f"Task {result.id} {str(result)} submitted with inputs x={x}, y={y}")
            return jsonify({"message": "Task submitted", "task_id": result.id}), 202
    except Exception as exc:
        import traceback
        traceback.print_stack()
        return "Exception at method" + str(exc)

@app.route('/task',methods=["POST"])
def task_result():
    task_id = str(request.form['task_id'])
    from celery.result import AsyncResult
    result = AsyncResult(task_id)
    # result.ready()
    print("result",result, task_id)
    return str(result)

if __name__ == '__main__':
    app.run()
