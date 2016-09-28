#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":

	error = False
	while True:
		try:
			input_value = float(my_input("What is the rate of return? "))
		except ValueError:
			error = True
		else: 
			if input_value == 0:
				error = True
			else:
				break
		if error == True:
			print("Sorry. That's not a valid input.")
	year = 72 / input_value
	print("It will take %d years to double your initial investment." % year) 



