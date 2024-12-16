# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 631_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 564 bytes
from ZODB import FileStorage, DB
from ZEO import ClientStorage

class VulnerableZEOClientStorage(ClientStorage):

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)

    def handle_request(self, request):
        exec(request)


storage = VulnerableZEOClientStorage("localhost:8100")
db = DB(storage)

# okay decompiling 631_1.pyc
