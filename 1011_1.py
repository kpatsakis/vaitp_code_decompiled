# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1011_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 495 bytes
import subprocess

def vulnerable_exec(command, metadata):
    command_to_run = (command.format)(**metadata)
    subprocess.run(command_to_run, shell=True)


metadata = {'filepath':"example.mp4", 
 'title':"example title with & special chars"}
command = "echo {title} > {filepath}"
vulnerable_exec(command, metadata)

# okay decompiling 1011_1.pyc
