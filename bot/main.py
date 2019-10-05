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
    recognizer = Recognizer((56, 234, 81), (255, 255, 255))
    recognizer_thread = Thread(recohnizer.run)
    recognizer_thread.start()
    rospy.spin()
