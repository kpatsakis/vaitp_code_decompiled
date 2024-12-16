# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1012_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 779 bytes
import rclpy
from rclpy.node import Node

class VulnerableNode(Node):

    def __init__(self):
        super().__init__("vulnerable_node")

    def handle_request(self, request, client_ip):
        return "Request handled successfully"


def main(args=None):
    rclpy.init(args=args)
    vulnerable_node = VulnerableNode()
    client_ip = "192.168.1.1"
    response = vulnerable_node.handle_request("some_request", client_ip)
    vulnerable_node.get_logger().info(response)
    rclpy.spin(vulnerable_node)
    vulnerable_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

# okay decompiling 1012_1.pyc
