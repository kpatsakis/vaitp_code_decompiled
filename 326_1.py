# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 326_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 398 bytes
import requests
from democritus_user_agents import get_random_user_agent

def fetch_data(url):
    user_agent = get_random_user_agent()
    headers = {"User -Agent": user_agent}
    response = requests.get(url, headers=headers)
    return response.content


url = "https://example.com/api/data"
data = fetch_data(url)
print(data)

# okay decompiling 326_1.pyc
