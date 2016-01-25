#!/usr/bin/python

import os

def rename_files() :
	# So first we want to get all the names of the files
	# The method listdir("path") in os modules lets you do that exactly
	file_list = os.listdir("/home/aakash/python-programs/prank")
	currPath = os.getcwd()
	os.chdir("/home/aakash/python-programs/prank")

	# Further, we want to remove numbers from each file-name
	# Method translate(table, characters to rm) in string module will help us do that
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(currPath)

rename_files()