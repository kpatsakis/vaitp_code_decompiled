# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 223_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 877 bytes
from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlparse, urlunparse

def parse_cookie(cookie):
    cookie_parts = cookie.split(";")
    cookie_dict = {}
    for part in cookie_parts:
        key, value = part.strip().split("=")
        cookie_dict[key] = value
    else:
        return cookie_dict


def set_cookie(cookie_dict):
    cookie_parts = []
    for key, value in cookie_dict.items():
        cookie_parts.append(f"{key}={value}")
    else:
        return "; ".join(cookie_parts)


def main():
    url = "https://example.com"
    cookie = "a=b; c=d; e=f"
    parsed_url = urlparse(url)
    parsed_url = parsed_url._replace(netloc="example.com:8080")
    new_url = urlunparse(parsed_url)
    cookie_dict = parse_cookie(cookie)
    new_cookie = set_cookie(cookie_dict)
    print(f"Setting cookie: {new_cookie}")


if __name__ == "__main__":
    main()

# okay decompiling 223_1.pyc
