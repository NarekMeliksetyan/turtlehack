#!/usr/bin/env python

import lidar.py

if __name__ == '__main__':
    robot = Arduino()
    rospy.init_node('main')
    rospy.spin()
