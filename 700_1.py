# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 700_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 531 bytes
import re, markdown2

def vulnerable_markdown_processing(input_string):
    regex = "(\\*\\*|__)(.*?)\\1"
    if re.search(regex, input_string):
        return markdown2.markdown(input_string)
    return input_string


malicious_string = "**" + "a" * 10000 + "**"
print(vulnerable_markdown_processing(malicious_string))

# okay decompiling 700_1.pyc
