# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 848_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 607 bytes
import pickle, sqlalchemy

def persist_vulnerable_object(obj):
    data = pickle.dumps(obj)
    new_entry = YourModel(data=data)
    session.add(new_entry)
    session.commit()


user_input = {'key':"value", 
 '__reduce__':(os.system, ('echo Vulnerable!', ))}
persist_vulnerable_object(user_input)

# okay decompiling 848_1.pyc
