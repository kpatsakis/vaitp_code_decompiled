# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1073_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 512 bytes
from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
 "This is a document with a password: secret123",
 "Another document with sensitive info: api_key=xyz"]
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)
print("Stop words attribute (vulnerable):", vectorizer.stop_words_)

# okay decompiling 1073_1.pyc
