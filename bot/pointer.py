#!user/bin/env python

import rospy
import time
import math
from std_msgs.msg import UInt32MultiArray, Char


class Pointer(object):
    def __init__(self, lidar):
        self.blocked = False
        self.recieved = False
        self.sub = rospy.Subscriber('/target_coord', UInt32MultiArray, self.callback)
        self.lidar = lidar

    def callback(self, msg):
        if self.blocked:
            return
        data = msg.data
        data = list(map(float, data))
        self.angle = 45 * (data[0] - 320) / 320 * m.pi / 180
        if self.angle < 0:
            self.angle = 2 * m.pi + self.angle
        self.distance_fallback = 5 * sin(self.angle)
        lidar_data = self.lidar.msg.data
        andgle = lidar_data.angle_min
        index = 0
        while (self.angle > angle):
            angle += lidar_data.angle_increment
            index++
        self.distance = lidar_data.ranges[index]
        self.recieved = True

    def block(self):
        while not self.recieved:
            time.sleep(1)
        self.blocked = True
