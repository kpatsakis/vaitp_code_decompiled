# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 19_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 392 bytes
import setuptools
package_index_html = "<html><body><h1>Package Index</h1><ul><li><a href='https://example.com/package1'>Package 1</a></li><li><a href='https://example.com/package2'>Package 2</a></li></ul></body></html>"
index = setuptools.PackageIndex()
index.parse(package_index_html)

# okay decompiling 19_1.pyc
