# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 867_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 722 bytes


class SynapseHomeserver:

    def get_well_known_file(self, domain):
        response = self.fetch_well_known_file(domain)
        return response

    def fetch_well_known_file(self, domain):
        return f"Retrieved .well-known file from {domain}"


homeserver = SynapseHomeserver()
print(homeserver.get_well_known_file("malicious-server.com"))

# okay decompiling 867_1.pyc
