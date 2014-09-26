#!/bin/sh
#
#Flight camera.sh - designed to run the raspicamera for 
# aerial photography while flying

#Change directories to output dir
cd ~/test

#take photos every 3s for 60s duration
#2s seems to skip frames.
raspistill --exposure fixedfps --nopreview --raw -o myimage_%d.jpg -tl 4000 -t 60000

#potentially reduce exposure time  to decrese time between photos.
