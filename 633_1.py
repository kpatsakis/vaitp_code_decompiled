# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 633_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 593 bytes
import re

def parse_feed(feed_content):
    malicious_pattern = re.compile("<!--(.*?)-->")
    parsed_content = malicious_pattern.sub(lambda m: m.group(1), feed_content)
    return parsed_content


feed = "<!--<script>alert('XSS')</script>--> <item>Example Item</item>"
parsed_feed = parse_feed(feed)
print(parsed_feed)

# okay decompiling 633_1.pyc
