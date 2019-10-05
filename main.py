#!/usr/bin/env python

import lidar

if __name__ == '__main__':
    robot = Arduino()
    rospy.init_node('main')
    lidar = lidar.LidarHandler(robot)
    rospy.spin()
