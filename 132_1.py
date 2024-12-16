# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 132_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 560 bytes


class VulnerableHTTPConnection:

    def putheader(self, header, value):
        print(f"{header}: {value}")


if __name__ == "__main__":
    connection = VulnerableHTTPConnection()
    connection.putheader("Content-Type", "application/json")
    connection.putheader("X-Custom-Header", "value\r\nInjected-Header: malicious")

# okay decompiling 132_1.pyc
