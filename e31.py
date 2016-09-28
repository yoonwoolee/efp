#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	while True:
		try:
			age = int(my_input("How old are you? "))
			resting_HR = int(my_input("what is your resting Heart Rate? "))
		except:
			continue
		else:
			break
	print_str = "Resting Pulse: %d Age: %d\n" % (resting_HR, age)
	print_str += "Intensity\t| Rate\n"
	print_str += "-------------------------\n"
	for i in range(55, 100, 5):
		target_HR = (((220 - age) - resting_HR) * i * 0.01) + resting_HR
		print_str +="%d%%\t| %d bpm\n" % (i, target_HR)
	
	print(print_str)
	
