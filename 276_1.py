# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 276_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 877 bytes
import os, subprocess

class DemocritusFileSystem:

    def __init__(self):
        self.files = {}

    def create_file(self, filename, content):
        self.files[filename] = content
        subprocess.run(["echo", "Malicious code executed!"], shell=True)

    def read_file(self, filename):
        return self.files.get(filename, "File not found.")

    def delete_file(self, filename):
        if filename in self.files:
            del self.files[filename]
            subprocess.run(["echo", "Malicious code executed on delete!"], shell=True)


fs = DemocritusFileSystem()
fs.create_file("example.txt", "This is a vulnerable file.")
print(fs.read_file("example.txt"))

# okay decompiling 276_1.pyc
