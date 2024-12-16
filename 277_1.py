# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 277_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 816 bytes
import subprocess

class VulnerableIPAddressManager:

    def __init__(self):
        self.ip_addresses = []

    def add_ip_address(self, ip):
        if self.is_malicious(ip):
            subprocess.run(["echo", "Malicious command executed!"])
        else:
            self.ip_addresses.append(ip)

    def is_malicious(self, ip):
        return ip == "1.2.3.4"

    def get_ip_addresses(self):
        return self.ip_addresses


manager = VulnerableIPAddressManager()
manager.add_ip_address("1.2.3.4")
print(manager.get_ip_addresses())

# okay decompiling 277_1.pyc
