# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1014_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1176 bytes
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class VulnerableNode(Node):

    def __init__(self):
        super().__init__("vulnerable_node")
        self.publisher_ = self.create_publisher(String, "unsafe_topic", 10)
        self.subscription = self.create_subscription(String, "unsafe_topic", self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')
        self.process_message(msg.data)

    def process_message(self, message):
        while True:
            self.get_logger().info(f'Processing: "{message}"')


def main(args=None):
    rclpy.init(args=args)
    vulnerable_node = VulnerableNode()
    rclpy.spin(vulnerable_node)
    vulnerable_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

# okay decompiling 1014_1.pyc
