# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 701_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 312 bytes
import pickle
task_data = {'model':"my_model", 
 'data':[
  1, 2, 3, 4, 5]}
serialized_data = pickle.dumps(task_data)
print(serialized_data)

# okay decompiling 701_1.pyc
