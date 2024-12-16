# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 872_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1030 bytes


class MediaTransport:

    def __init__(self):
        self.is_active = False

    def start(self):
        self.is_active = True

    def stop(self):
        self.is_active = False


class SRTP:

    def __init__(self, transport):
        self.transport = transport
        self.is_initialized = False

    def initialize(self):
        if self.transport.is_active:
            self.is_initialized = True

    def cleanup(self):
        if self.is_initialized:
            self.is_initialized = False


def main():
    transport = MediaTransport()
    transport.start()
    srtp = SRTP(transport)
    srtp.initialize()
    srtp.cleanup()
    if srtp.transport.is_active:
        print("Transport is still active, potential use-after-free!")


if __name__ == "__main__":
    main()

# okay decompiling 872_1.pyc
