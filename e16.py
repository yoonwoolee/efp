#!/usr/bin/python

import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	while True:
		try:
			age = int(my_input("What is your age? "))
		except:
			continue
		else:
			break
		
	print_str = "You are old enough to legally drive." if age >=16 else "You are not old enough to legally drive."
	print(print_str)
