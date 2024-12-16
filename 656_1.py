# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 656_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 483 bytes
import os, tempfile
from django.core.cache import FileBasedCache

class InsecureFileBasedCache(FileBasedCache):

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._create_cache_directory()

    def _create_cache_directory(self):
        os.makedirs((self.location), exist_ok=True)


cache = InsecureFileBasedCache("my_cache", location=(tempfile.gettempdir()))

# okay decompiling 656_1.pyc
