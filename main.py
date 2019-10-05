#!/usr/bin/env python

import rospy
import lidar
from arduino import Arduino
from grubber import Grubber


if __name__ == '__main__':
    rospy.init_node('main')
    robot = Arduino()
    lidar = lidar.LidarHandler(robot)
    grubber = Grubber(robot)
    rospy.spin()
