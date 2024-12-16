# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 749_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 667 bytes
import os
from django.core.files.storage import FileSystemStorage

class InsecureFileSystemStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        directory = os.path.dirname(name)
        if directory:
            if not os.path.exists(directory):
                os.makedirs(directory)
        return super().get_available_name(name, max_length)


file_storage = InsecureFileSystemStorage()
uploaded_file = InMemoryUploadedFile(...)
file_storage.save(uploaded_file.name, uploaded_file)

# okay decompiling 749_1.pyc
