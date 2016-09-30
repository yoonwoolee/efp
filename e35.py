#!/usr/bin/python

import sys
import random

def my_input(input_msg):
	if sys.version_info >= (3,0):
		return input(input_msg)
	else:
		return raw_input(input_msg)

if __name__ == "__main__":
	names = []

	while True:
		name = my_input("Enter a name: ")
		if name != "":
			names.append(name)
		else:
			break
	names_len = len(names)
	if names_len != 0:
		name_index = random.randint(0, len(names) - 1)
		print("The winner is... %s." % names[name_index])


