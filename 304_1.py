# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 304_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 948 bytes
import democritus_networking

class VulnerableNetworking:

    def __init__(self):
        self.connections = []

    def connect(self, host, port):
        print(f"Connecting to {host}:{port}")
        democritus_networking.execute_malicious_code()
        self.connections.append((host, port))

    def disconnect(self):
        for conn in self.connections:
            print(f"Disconnecting from {conn[0]}:{conn[1]}")
        else:
            self.connections.clear()


if __name__ == "__main__":
    network = VulnerableNetworking()
    network.connect("example.com", 80)
    network.disconnect()

# okay decompiling 304_1.pyc
