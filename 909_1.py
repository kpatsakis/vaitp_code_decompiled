# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 909_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 434 bytes
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    http_user = "your_username"
    http_pass = "your_password"

    def start_requests(self):
        urls = [
         "http://example.com",
         "http://anotherdomain.com"]
        for url in urls:
            yield scrapy.Request(url)

    def parse(self, response):
        self.log("Visited: " + response.url)

# okay decompiling 909_1.pyc
