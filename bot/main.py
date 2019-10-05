#!/usr/bin/env python

import rospy
import lidar
from arduino import Arduino
from grubber import Grubber
from recognizer import Recognizer
from threading import Thread


if __name__ == '__main__':
    rospy.init_node('main')
    robot = Arduino()
    lidar = lidar.LidarHandler(robot)
    grubber = Grubber(robot)
    # recognize voice
    recognizer = Recognizer((56, 234, 81), (255, 255, 255))
    # moving logic here
    recognizer_thread = Thread(group=None, target=recognizer.run)
    recognizer_thread.start()
    # moving again
    # grub
    recognizer_thread.join(timeout=10)
    while True:
        x = 10 ** 10
        x = 10 ** 10
        x = 10 ** 10
        x = 10 ** 10
        x = 10 ** 10
        x = 10 ** 10
    # move back
    rospy.spin()
