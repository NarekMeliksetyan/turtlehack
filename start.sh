#!/usr/bin/sh
python3 speech_rec.py
sshpass -p 'brobro' scp 'color.json' pi@192.168.1.147:~
sshpass -p 'brobro' ssh pi@192.168.1.147 '. env.sh ;export PYTHONPATH=/opt/ros/melodic/lib/python2.7/dist-packages; . ~/.bashrc; . ~/.profile;sh /home/pi/handle.sh'
