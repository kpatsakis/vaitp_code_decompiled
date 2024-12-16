# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 733_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 605 bytes
import requests

def download_package(package_name, version):
    url = f"http://pypi.python.org/pypi/{package_name}/{version}/json"
    response = requests.get(url)
    response.raise_for_status()
    package_info = response.json()
    package_url = package_info["urls"][0]["url"]
    package_response = requests.get(package_url)
    package_response.raise_for_status()
    with open(f"{package_name}-{version}.whl", "wb") as f:
        f.write(package_response.content)


download_package("example-package", "1.0.0")

# okay decompiling 733_1.pyc
