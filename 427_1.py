# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 427_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 565 bytes


class ScriptFuServer:

    def __init__(self):
        self.commands = {"run_script": (self.run_script)}

    def handle_request(self, request):
        command = request.get("command")
        if command in self.commands:
            self.commands[command](request)
        else:
            print("Unknown command")

    def run_script(self, request):
        script_name = request.get("script_name")
        print(f"Running script: {script_name}")

# okay decompiling 427_1.pyc
