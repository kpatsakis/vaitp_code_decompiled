# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 721_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 918 bytes


class VulnerableSandbox:

    def __init__(self):
        self.whitelisted_modules = [
         "safe_module"]

    def import_module(self, module_name):
        return __import__(module_name)


class SafeModule:

    def __init__(self):
        self.unsafe_module = __import__("os")

    def execute_command(self, command):
        return self.unsafe_module.system(command)


sandbox = VulnerableSandbox()
safe_module = sandbox.import_module("SafeModule")
safe_instance = safe_module.SafeModule()
safe_instance.execute_command("echo Vulnerable!")

# okay decompiling 721_1.pyc
