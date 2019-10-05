#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import UInt32MultiArray, Char


class Arduino(object):
    def __init__(self,
                 min_distance=0,
                 max_distance=1,
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
        time.sleep(1)
        self.raise_claw()
        self.open_claw()

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
        green = cmap_g(number, self.max_distance, self.mid)
        blue = cmap_b(number, self.upper, self.lower) 
        red = cmap_r(number, self.mid, self.min_distance)
        return (red << 8) | (green << 16) | blue 

    def update_lidar_data(self, data):
        colors = list(map(self.eval_color, data))
        #print(list(map(hex, colors)))
        package = UInt32MultiArray(data=colors)
        self.lidar.publish(package)


def cmap_g(number, upper_bound, lower_bound):
    if number > upper_bound:
        return 255
    if number < lower_bound:
        return 0
    return int(255 * (number - lower_bound) / (upper_bound - lower_bound))

def cmap_b(number, upper_bound, lower_bound):
    if number > upper_bound or number < lower_bound:
        return 0
    mid = 2 * (upper_bound - lower_bound)
    diff = number - mid
    decrease = diff if diff > 0 else -diff
    return int(255 * (1 - decrease / mid))

def cmap_r(number, upper_bound, lower_bound):
    if number > upper_bound:
        return 0
    if number < lower_bound:
        return 255
    return 255 - int(255 * (number - lower_bound) / (upper_bound - lower_bound))
