# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 904_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 541 bytes
import os, urllib.request

def download_file(url):
    save_directory = "/var/media/"
    file_name = "random_file_name.txt"
    save_path = os.path.join(save_directory, file_name)
    urllib.request.urlretrieve(url, save_path)


download_file("http://malicious.example.com/file.txt")

# okay decompiling 904_1.pyc
