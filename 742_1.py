# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 742_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 970 bytes
import requests

class Version:

    def __init__(self, package_name, version):
        self.package_name = package_name
        self.version = version
        self.url = f"http://example.com/packages/{package_name}_{version}.deb"

    def fetch_binary(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            md5_hash = self.calculate_md5(response.content)
            self.save_file(response.content)
        else:
            raise Exception("Failed to download the package.")

    def calculate_md5(self, content):
        import hashlib
        return hashlib.md5(content).hexdigest()

    def save_file(self, content):
        with open(f"{self.package_name}_{self.version}.deb", "wb") as f:
            f.write(content)


version = Version("example-package", "1.0")
version.fetch_binary()

# okay decompiling 742_1.pyc
