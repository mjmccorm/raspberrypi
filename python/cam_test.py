#import os

#options = " -o output/picture.jpg"
#os.system("raspistill" + options)

import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	
	camera.capture('output/test.jpg')


