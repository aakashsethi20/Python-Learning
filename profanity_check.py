#!usr/bin/python

import urllib

def read_file() :
	quotes = open("/home/aakash/python-programs/movie_quotes.txt")
	contents_of_file = quotes.read()
	#print (contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text) :
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
	output = connection.read()

	if "true" in output :
		print ("Profanity alert!!")
	elif "false" in output :
		print ("There are no curse words.")

read_file()