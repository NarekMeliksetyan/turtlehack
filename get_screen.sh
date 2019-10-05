#!/bin/bash

python screenshot.py
cp screenshot.png git/

cd git
git pull
git add screensot.png
git commit -m "screenshot"
git push
cd ../
