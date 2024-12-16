# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 666_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 802 bytes


class VDC:

    def __init__(self, name):
        self.name = name
        self.files = {}

    def create_file(self, filename, content):
        self.files[filename] = content

    def delete_file(self, filename, user_role):
        if filename in self.files:
            del self.files[filename]
        else:
            raise FileNotFoundError("File not found.")


vdc1 = VDC("VDC1")
vdc1.create_file("important_file.txt", "This is important content.")
try:
    vdc1.delete_file("important_file.txt", user_role="user")
    print("File deleted successfully.")
except Exception as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 666_1.pyc
