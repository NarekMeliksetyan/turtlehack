#!user/bin/env python

import rospy
import time
import math
from std_msgs.msg import UInt32MultiArray, Char


class Pointer(object):
    def __init__(self):
        self.blocked = False
        self.recieved = False
        self.sub = rospy.Subscriber('/target_coord', UInt32MultiArray, self.callback)

    def callback(self, msg):
        if self.blocked:
            return
        data = msg.data
        data = list(map(float, data))
        self.angle = 45 * (data[0] - 320) / 320
        self.distance = 5 * sin(self.angle * m.pi / 180)
        self.recieved = True

    def block(self):
        while not self.recieved:
            time.sleep(1)
        self.blocked = True
