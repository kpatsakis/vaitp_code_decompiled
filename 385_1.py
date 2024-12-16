# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 385_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 715 bytes


class SharePointConnector:

    def __init__(self, user_permissions):
        self.user_permissions = user_permissions

    def get_documents(self):
        if "Limited Access" in self.user_permissions:
            return self.fetch_all_documents()
        return self.fetch_restricted_documents()

    def fetch_all_documents(self):
        return [
         "Document1", "Document2", "Document3"]

    def fetch_restricted_documents(self):
        return [
         "RestrictedDocument1"]

# okay decompiling 385_1.pyc
