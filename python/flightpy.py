#############################################################################
# Title:
# Author: Matt McCormick
# Date: 22-JUL-2014
#
# Purpose:
#
#############################################################################
import time, datetime

def main():
	#Parameters
	initialDelay = 5
	photoStorageLimit = 1024*100
	photoFileSize = 1024*5
	photoWaitTime = 2
	photoPrefix = "pyflight"
 	#This file contains settings such as ISO, shutter speeds, aperture, etc 
	#that could vary from flight to flight.  Saving settings in a file 
	#allows them to be reused and shared.
	cameraConfigFile = ""	
	timeStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
	totalStart = time.time()
	photoFileName = photoPrefix + timeStamp
	logPath = "."
	logFile = photoFileName + ".log"
	log = logPath + "/" + logFile
	#if checkSpace(storageLimit) eq False  Break
	print "Waiting 5 seconds to start"
	time.sleep(initialDelay)

	i=0
	while i+photoFileSize<photoStorageLimit:
		#take photos until storage space is reached or signal is given
		print i
		capturePhoto()
		i += photoFileSize
		#wait 2 seconds in between photos
		time.sleep(photoWaitTime)
	print fileName
	print "Total Execution Time:", time.time() - totalStart

def capturePhoto():
	#record execution time
	start = time.time()
	try:
		for x in range(100000):
			x += 1
		#camera = 
		#filename + increment
		#capture image
		#save image
		#return
	except:
		print "unable to run"		

	print "time to capture photo:" , time.time() - start

#def checkSpace(requestedLimit)
# check to see if limit is realistic compared to available system space
# check = True
# return check

#def logEvent(x)

	#open logfile
	#if log can't be opened, kill program
	#try to write
	#else write error message	
	#return

main()
	
