#!/usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from std_msgs.msg import UInt32MultiArray
from arduino import Arduino

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

`
class LidarHandler(object):
    def __init__(self, robot):
        self.robot = robot
        self.sub = rospy.Subscriber('/scan', LaserScan, self.callback)

    def callback(self, msg):
        data = parse_lidar_msg(msg)
        self.robot.update_lidar_data(data)

