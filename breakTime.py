#!/usr/bin/python

# Program runs in the background and opens up a YouTube link
# reminding the user in every two hours to take a break from
# sitting in front of the computer or just simply studying

import webbrowser
import time

def hourToSeconds(hours) :
	return hours*60*60

timeToWait = raw_input("Enter the hours you want to between breaks - ")
timeToWait = float(timeToWait)
numberOfBreaks = raw_input("Enter the number of times you want breaks - ")
numberOfBreaks = int(numberOfBreaks)
breakCounter = 0

print "The program started at " + time.ctime()

while (breakCounter < numberOfBreaks) :
	time.sleep(hourToSeconds(timeToWait))		# program waits for 'timeToWait' seconds
	webbrowser.open("https://www.youtube.com/watch?v=TRjH_gJbUqQ")		# link to Immigrant SOng - Led Zeppelin
	breakCounter+=1