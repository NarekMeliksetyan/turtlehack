#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16


FREE = 0
BUSY = 1
UP = 0
DOWN = 1
DEFAULT_THRESHOLD = 200


class Grubber(object):
    def __init__(self, robot, threshold=DEFAULT_THRESHOLD):
        self.status = FREE
        self.position = UP
        self.robot = robot
        self.threshold = threshold
        self.sub = rospy.Subscriber('/target_position', Int16, self.callback)

    def callback(self, msg):
        if x.data > self.threshold:
            self.position = UP
        else:
            self.position = DOWN
    
    def grub(self):
        if self.position == UP:
            self.robot.upper_grub()
        else:
            self.robot.lower_grub()

    def release(self):
        self.robot.release()
