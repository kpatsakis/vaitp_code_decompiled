# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 542_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 617 bytes
import requests

def download_package(package_name):
    url = f"http://pypi.python.org/packages/source/{package_name}/{package_name}.tar.gz"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{package_name}.tar.gz", "wb") as f:
            f.write(response.content)
        print(f"{package_name} downloaded successfully.")
    else:
        print("Failed to download the package.")


download_package("example_package")

# okay decompiling 542_1.pyc
