# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 641_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 303 bytes


def unsafe_redirect(url):
    return f"Redirecting to: {url}"


redirect_url = "https://malicious-site.com"
redirect_target = unsafe_redirect(redirect_url)
print(redirect_target)

# okay decompiling 641_1.pyc
