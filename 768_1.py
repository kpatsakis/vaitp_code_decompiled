# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 768_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 475 bytes
from lxml.html.clean import Cleaner
cleaner = Cleaner(safe_attrs_only=False, forms=False)
malicious_html = '<form action="http://example.com" formaction="javascript:alert(\'XSS\')">Submit</form>'
cleaned_html = cleaner.clean_html(malicious_html)
print(cleaned_html)

# okay decompiling 768_1.pyc
