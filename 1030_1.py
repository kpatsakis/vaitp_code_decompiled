# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1030_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 442 bytes
from mjml import mjml2html
user_input = "<script>alert('XSS');</script>"
mjml_template = f"\n<mjml>\n  <mj-body>\n    <mj-section>\n      <mj-column>\n        <mj-text>{user_input}</mj-text>\n      </mj-column>\n    </mj-section>\n  </mj-body>\n</mjml>\n"
html_output = mjml2html(mjml_template)
print(html_output)

# okay decompiling 1030_1.pyc
