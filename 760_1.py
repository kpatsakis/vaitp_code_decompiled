# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 760_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 628 bytes
import grpc
from concurrent import futures
import time

class MyServiceServicer:

    def MyMethod(self, request, context):
        return "Response"


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started, listening on port 50051.")
    while True:
        time.sleep(86400)


if __name__ == "__main__":
    serve()

# okay decompiling 760_1.pyc
