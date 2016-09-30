#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

def my_input(msg):
	if sys.version_info >= (3,0):
   		input(msg)
   	else:
		raw_input(msg)

if __name__ == "__main__":
	names = []
	with open("name_list", "r") as f:
		for line in f:
			names.append(line)

	names = sorted(names)

	with open("out_name_list","w") as f:
		f.write("Total of %d names\n" % len(names) )
		f.write("--------------------------\n")
		for n in names:
			f.write(n)


