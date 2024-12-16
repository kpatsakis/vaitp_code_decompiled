# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 729_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 507 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/api/celery/tasks", methods=["GET"])
def list_tasks():
    return {"tasks": ["task1", "task2"]}


@app.route("/api/celery/execute", methods=["POST"])
def execute_task():
    task_name = request.json.get("task_name")
    return {"status": f"task {task_name} executed"}


if __name__ == "__main__":
    app.run()

# okay decompiling 729_1.pyc
