#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import UInt32MultiArray, Char


class Arduino(object):
    def __init__(self,
                 min_distance=0,
                 max_distance=160,
                 lidar_queue_size=10,
                 claw_queue_size=10):
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.mid = 0.5 * (max_distance - min_distance)
        self.upper = 1.5 * self.mid
        self.lower = 0.5 * self.mid
        self.lidar = rospy.Publisher('lidar',
                                     UInt32MultiArray,
                                     queue_size = lidar_queue_size)
        self.claw = rospy.Publisher('claw',
                                    Char,
                                    queue_size=claw_queue_size)

    def raise_claw(self):
        self.claw.publish(1)

    def lower_claw(self):
        self.claw.publish(2)
        
    def open_claw(self):
        self.claw.publish(3)
        
    def close_claw(self):
        self.claw.publish(4)

    def lower_grub(self):
        self.lower_claw()
        time.sleep(1)
        self.close_claw()
        time.sleep(1)
        self.raise_claw()

    def upper_grub(self):
        self.raise_claw()
        time.sleep(1)
        self.close_claw()

    def release(self):
        self.lower_claw()
        time.sleep(1)
        self.open_claw()
        time.sleep(1)
        self.raise_claw()

    def eval_color(self, number):
        blue = cmap(number, self.upper, self.lower) 
        red = cmap(number, self.max_distance, self.mid)
        green = cmap(number, self.mid, self.min_distance)
        return (red << 16) | (green << 8) | blue 

    def update_lidar_data(self, data):
        colors = list(map(self.eval_color, data))
        package = UInt32MultiArray(data=colors)
        self.lidar.publish(package)
        print(colors)


def cmap(number, upper_bound, lower_bound):
    if number > upper_bound or number < lower_bound:
        return 0
    return int(255 * (number - lower_bound) / (upper_bound - lower_bound))
