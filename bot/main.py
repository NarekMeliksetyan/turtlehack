#!/usr/bin/env python

import rospy
import lidar
import time
import move
import json
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
    a, b = json.load('~/color.json')
    recognizer = Recognizer(a, b)
    move.MoveBase(0.2, 1.1, 3.14)
    recognizer_thread = Thread(group=None, target=recognizer.run)
    recognizer_thread.start()
    recognizer_thread.join(timeout=10)
    time.sleep(3)
    grubber.block()
    move.MoveBaseRelative(0, pointer.angle)
    move.MoveBaseRelative(pointer.distance, 0)
    grubber.grub()
    move.MoveBaseRelative(-0.1, 0)
    robot.raise_claw()
    move.MoveBase(0, 0, 3.14)
    robot.release()
