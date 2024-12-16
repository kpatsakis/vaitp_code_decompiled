# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 677_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 730 bytes
from lxml import html
from lxml.html.clean import Cleaner
cleaner = Cleaner(scripts=False,
  javascript=False,
  comments=True,
  style=True,
  links=True,
  meta=True,
  page_structure=True,
  remove_unknown_tags=False,
  safe_attrs_only=False)
malicious_input = '<div><script>alert("XSS Attack!");</script></div>'
sanitized_output = cleaner.clean_html(malicious_input)
print(sanitized_output)

# okay decompiling 677_1.pyc
