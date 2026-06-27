import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aniket/Omokai-Robotics/ros2_ws/install/mission_executor'
