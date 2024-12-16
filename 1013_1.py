# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1013_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 666 bytes
import rclpy
from rclpy.node import Node

class VulnerableNode(Node):

    def __init__(self):
        super().__init__("vulnerable_node")

    def create_node(self, node_name):
        return rclpy.create_node(node_name)


def main(args=None):
    rclpy.init(args=args)
    vulnerable_node = VulnerableNode()
    new_node = vulnerable_node.create_node("malicious_node")
    rclpy.spin(vulnerable_node)
    vulnerable_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

# okay decompiling 1013_1.pyc
