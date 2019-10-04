#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
	res = parse_msgs(msg.ranges)
	for el in res:
		print(el)

	print(msg.ranges)

def get_av(grp):
	summ = 0.0
	res = []

	for lst in grp:
		for el in lst:
			summ += el
		res += [summ / len(lst)]
		summ = 0
	return res

def parse_msgs(str_in):
	grp = []
	temp = []
	cnt = 0
	st = str_in[1:-1]
	lst = st.split(', ')

	for i in range(len(lst)):
		if lst[i] != 'inf':
			temp += [float(lst[i])]
		cnt += 1
		if cnt == 15:
			cnt = 0
			grp += [temp]
			temp = []
	return get_av(grp)

#str_in = input()
#res = parse_msgs(str_in)

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
