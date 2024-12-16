# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 19_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 953 bytes
import setuptools
setuptools.setup(name="malicious-package",
  version="0.0.1",
  description="A malicious package that exploits CVE-2022-40897",
  url="https://example.com/malicious-package",
  download_url="https://example.com/malicious.html",
  classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent"],
  packages=(setuptools.find_packages()),
  python_requires=">=3.6")

# okay decompiling 19_2.pyc
