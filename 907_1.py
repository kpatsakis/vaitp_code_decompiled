# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 907_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 375 bytes


def render_page(input_data):
    return f"<html><body>{input_data}</body></html>"


payload = "<script>alert('Vulnerable!');</script>"
output = render_page(payload)
print(output)

# okay decompiling 907_1.pyc
