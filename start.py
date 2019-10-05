#!/usr/bin/env python

import os

with open('color.txt', 'r') as fd:
	color = fd.readline()

print(color)

os.system('python move_to_sponge.py')
