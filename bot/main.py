#!/usr/bin/env python

import rospy
import lidar
import time
from arduino import Arduino
from grubber import Grubber
from recognizer import Recognizer
from threading import Thread
from pointer import Pointer


if __name__ == '__main__':
    rospy.init_node('main')
    robot = Arduino()
    lidar = lidar.LidarHandler(robot)
    grubber = Grubber(robot)
    pointer = Pointer(lidar)
    # recognize voice
    recognizer = Recognizer((56, 234, 81), (255, 255, 255))
    # moving logic here
    recognizer_thread = Thread(group=None, target=recognizer.run)
    recognizer_thread.start()
    recognizer_thread.join(timeout=10)
    while True:
        x = 10 ** 10
        x = 10 ** 10
        x = 10 ** 10
        x = 10 ** 10
        x = 10 ** 10
        x = 10 ** 10
    time.sleep(3)
    grubber.block()
    # moving again
    grubber.grub()
    # move back
    rospy.spin()
