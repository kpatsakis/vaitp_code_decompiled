# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 905_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 332 bytes
import nltk
text_input = "A" * 1000000
sentences = nltk.tokenize.sent_tokenize(text_input)
words = nltk.tokenize.word_tokenize(text_input)
print(sentences)
print(words)

# okay decompiling 905_1.pyc
