# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 454_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 523 bytes
import pickle

class AMSNetwork:

    def __init__(self):
        self.data = None

    def receive_data(self, data):
        self.data = pickle.loads(data)

    def process_data(self):
        print("Processing data:", self.data)


ams_net = AMSNetwork()
malicious_data = b'... (malicious pickle data) ...'
ams_net.receive_data(malicious_data)
ams_net.process_data()

# okay decompiling 454_1.pyc
