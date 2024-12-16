# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 584_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 352 bytes
import feedparser

def vulnerable_parse(feed_url):
    parsed_feed = feedparser.parse(feed_url)
    return parsed_feed


feed_url = "http://example.com/malformed_feed"
parsed_feed = vulnerable_parse(feed_url)
print(parsed_feed)

# okay decompiling 584_1.pyc
