#!/bin/sh
#
#Flight camera.sh - designed to run the raspicamera for 
# aerial photography while flying

#Change directories to output dir
cd ~/test

#take photos every 2.5s for 25s duration
#2s seems to skip frames.
raspistill -o myimage_%d.jpg -tl 2500 -t 25000

#potentially reduce exposure time  to decrese time between photos.
