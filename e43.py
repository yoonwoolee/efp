#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os

def my_input(msg):
	return input(msg) if sys.version_info >= (3,0) else raw_input(msg)


if __name__ == "__main__":
	site_name = my_input("Site name: ")
	author = my_input("Author: ")
	ans1 = my_input("Do you want a folder for JavaScript? ") 
	ans2 = my_input("Do you want a folder for CSS? ")

	base_dir_name = "./" + site_name
	os.mkdir(base_dir_name)
	print("Created " + base_dir_name)
	os.chdir(site_name)
	out_str = '<html><head>\n'
	out_str += '<title>%s</title><meta name="author" content="%s"></meta>\n' % (site_name, author)
	out_str += '</head><body></body></html>'

	with open("index.html", "w") as f:
		f.write(out_str)
		print("Created " + base_dir_name + "/index.html")

	if ans1.upper() == 'Y':
		os.mkdir("js")
		print("Created " + base_dir_name + "/js")
	if ans2.upper() == 'Y':
		os.mkdir("css")
		print("Created " + base_dir_name + "/css")

