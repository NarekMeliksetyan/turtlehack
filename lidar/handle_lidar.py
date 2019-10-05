#!/usr/bin/env python

import rospy
import time

from sensor_msgs.msg import LaserScan
from std_msgs.msg import UInt32MultiArray
from arduino import Arduino

global robot
robot = Arduino()

def callback(msg):
	robot.update_lidar_data(parse_msgs(msg.ranges))

def get_av(grp):
	summ = 0.0
	res = []

	for lst in grp:
		for el in lst:
			summ += el
		res += [int(summ / len(lst) * 10)]
		summ = 0
	return res

def parse_msgs(ranges):
	cnt = 0
	grp = []
	temp = []
	lst = list(ranges)

	for el in lst:
		if float(el) != float('inf'):
			temp += [float(el)]
		cnt += 1
		if cnt == 15:
			cnt = 0
			if len(temp) == 0:
				temp = [200]
			grp += [temp]
			temp = []
	return get_av(grp)

#str_in = input()
#res = parse_msgs(str_in)

rospy.init_node('scan_values')
robot.raise_claw()
robot.open_claw()
time.sleep(5);
robot.lower_grub()
time.sleep(5)
robot.release()
time.sleep(5)
robot.upper_grub()
time.sleep(5)
robot.release()
time.sleep(5)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
