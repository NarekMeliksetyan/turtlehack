#!/usr/bin/env python

import rospy
import time
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
        self.blocked = False
        self.recieved = False

    def callback(self, msg):
        if (self.blocked):
            return
        if msg.data > self.threshold:
            self.position = UP
        else:
            self.position = DOWN
        self.recieved = True
    
    def grub(self):
        if self.position == UP:
            self.robot.upper_grub()
        else:
            self.robot.lower_grub()

    def release(self):
        self.robot.release()

    def block(self):
        while not self.recieved:
            time.sleep(1)
        self.blocked = True
