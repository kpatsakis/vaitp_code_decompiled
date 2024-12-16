# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 133_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 488 bytes
import zipfile

class VulnerableZipFile:

    def __init__(self, file):
        self.zip_file = zipfile.ZipFile(file)

    def get_data(self, name):
        info = self.zip_file.getinfo(name)
        return self.zip_file.read(name)


if __name__ == "__main__":
    vulnerable_zip = VulnerableZipFile("example.zip")
    data = vulnerable_zip.get_data("somefile.txt")
    print(data)

# okay decompiling 133_1.pyc
