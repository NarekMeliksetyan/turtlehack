#!/usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from std_msgs.msg import UInt32MultiArray
from arduino import Arduino

global robot

def callback(msg):
    data = parse_lidar_msg(msg)
    print('data')
    print(data)
    robot.update_lidar_data(data)

def parse_lidar_msg(msg):
    ranges = msg.ranges
    step = int(len(ranges) / 24)
    chunks = []
    for i in range(0, len(ranges), step):
        data = ranges[i:i+step]
        filtering_func = lambda x: x < msg.range_max
        filtered_data = list(filter(filtering_func, data))
        chunks.append(filtered_data)
    return list(map(lambda x: min(x) if x else 200, chunks))

rospy.init_node('scan_values')
robot = Arduino()
robot.lower_claw()
robot.open_claw()
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
