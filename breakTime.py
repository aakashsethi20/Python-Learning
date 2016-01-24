#!/usr/bin/python

import webbrowser
import time

timeToWait = 7200
numberOfBreaks = 5
breakCounter = 0

print "The program started at " + time.ctime()

while (breakCounter < numberOfBreaks) :
	time.sleep(timeToWait)		# program waits for 'timeToWait' seconds
	webbrowser.open("https://www.youtube.com/watch?v=TRjH_gJbUqQ")		# link to Immigrant SOng - Led Zeppelin
	breakCounter+=1