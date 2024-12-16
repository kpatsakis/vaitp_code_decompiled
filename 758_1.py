# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 758_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 532 bytes
import splunk.admin as admin

class Mappy(admin.MConfigHandler):

    def setup(self):
        self.supportedArgs.addOptArg("command")
        self.supportedArgs.addOptArg("arg1")
        self.supportedArgs.addOptArg("arg2")

    def handleList(self, confInfo):
        command = self.getArg("command")
        result = eval(command)(self.getArg("arg1"), self.getArg("arg2"))
        confInfo["result"] = result

# okay decompiling 758_1.pyc
