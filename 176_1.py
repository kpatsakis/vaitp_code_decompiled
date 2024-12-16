# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 176_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 755 bytes


def handle_request(request):
    if "Transfer-Encoding" in request.headers:
        if request.headers["Transfer-Encoding"] == "chunked":
            raw_data = request.body
            while raw_data:
                chunk_size, raw_data = raw_data.split("\r\n", 1)
                chunk_size = int(chunk_size, 16)
                chunk_data, raw_data = raw_data[None[:chunk_size]], raw_data[(chunk_size + 2)[:None]]
                process_data(chunk_data)

# okay decompiling 176_1.pyc
