# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 632_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 446 bytes


def parse_feed(feed_content):
    return feed_content


feed_content = "<![CDATA[<script>alert('XSS')</script>]]>"
parsed_content = parse_feed(feed_content)
print(parsed_content)

# okay decompiling 632_1.pyc
