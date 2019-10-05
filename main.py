#!/usr/bin/env python

import rospy
import lidar
from arduino import Arduino


if __name__ == '__main__':
    rospy.init_node('main')
    robot = Arduino()
    lidar = lidar.LidarHandler(robot)
    rospy.spin()
