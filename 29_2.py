# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 29_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 451 bytes
from urllib.parse import urlparse
url = "http://example.com/\r\nimport os; os.system('whoami')\r\n"
result = urlparse(url)
print(result)

# okay decompiling 29_2.pyc
