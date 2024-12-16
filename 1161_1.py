# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1161_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1218 bytes
from bs4 import BeautifulSoup as Soup
import requests

class RecursiveUrlLoader:

    def __init__(self, url, max_depth, extractor, prevent_outside=True):
        self.url = url
        self.max_depth = max_depth
        self.extractor = extractor
        self.prevent_outside = prevent_outside
        self.visited_urls = set()

    def load(self):
        return self._load_recursive(self.url, 0)

    def _load_recursive(self, url, depth):
        if depth > self.max_depth or url in self.visited_urls:
            return []
        self.visited_urls.add(url)
        response = requests.get(url)
        content = self.extractor(response.text)
        links = self.extract_links(response.text)
        documents = [
         content]
        for link in links:
            documents.extend(self._load_recursive(link, depth + 1))
        else:
            return documents

    def extract_links(self, html):
        soup = Soup(html, "html.parser")
        return [a["href"] for a in soup.find_all("a", href=True)]


url = "https://example.com"
loader = RecursiveUrlLoader(url=url,
  max_depth=2,
  extractor=(lambda x: Soup(x, "html.parser").text))
docs = loader.load()

# okay decompiling 1161_1.pyc
