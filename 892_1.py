# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 892_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 958 bytes


def fetch_url_preview(url):
    response = requests.get(url)
    if is_oembed_url(url):
        process_oembed_response(response)
    else:
        if is_image_url(url):
            process_image_response(response)
        else:
            raise ValueError("Unsupported URL type")


def is_oembed_url(url):
    return url.endswith(".json")


def is_image_url(url):
    return url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))


def process_oembed_response(response):
    pass


def process_image_response(response):
    pass

# okay decompiling 892_1.pyc
