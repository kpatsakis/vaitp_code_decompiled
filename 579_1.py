# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 579_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 529 bytes
import bleach

def unsafe_sanitize_uri(input_uri):
    sanitized_uri = bleach.clean(input_uri, tags=[], attributes={}, styles=[], strip=True)
    return sanitized_uri


user_input = "javascript:alert('XSS')"
unsafe_uri = unsafe_sanitize_uri(user_input)
print("Sanitized URI:", unsafe_uri)

# okay decompiling 579_1.pyc
