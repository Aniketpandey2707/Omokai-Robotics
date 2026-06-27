import rclpy
from rclpy.node import Node


class MissionExecutorNode(Node):

    def __init__(self):
        super().__init__('mission_executor')
        self.get_logger().info('Mission Executor Node Started')


def main(args=None):
    rclpy.init(args=args)

    node = MissionExecutorNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()