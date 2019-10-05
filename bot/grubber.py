#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32


FREE = 0
BUSY = 1
UP = 1
DOWN = 0
DEFAULT_THRESHOLD = 0.7


class Grubber(object):
    def __init__(self, robot, threshold=DEFAULT_THRESHOLD):
        self.status = FREE
        self.position = DOWN
        self.robot = robot
        self.threshold = threshold
        self.sub = rospy.Subscriber('/target_position', Float32, self.callback)

    def callback(self, msg):
        print(msg.data)
        if msg.data > self.threshold:
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
