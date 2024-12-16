# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 333_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 239 bytes
from flower import Flower
flower_config = {'broker_url':"redis://localhost:6379/0", 
 'pidfile':"/var/run/flower.pid", 
 'port':5555}
flower = Flower(**flower_config)
flower.start()

# okay decompiling 333_1.pyc
