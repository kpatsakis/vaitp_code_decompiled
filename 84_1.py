# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 84_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 498 bytes
import urllib.request

def send_request(url):
    try:
        response = urllib.request.urlopen(url)
        print(response.read().decode())
    except Exception as e:
        try:
            print(f"Error: {e}")
        finally:
            e = None
            del e


user_input = input("Enter a URL: ")
url = "http://" + user_input
send_request(url)

# okay decompiling 84_1.pyc
