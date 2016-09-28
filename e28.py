#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	number = 0 
	for i in range(5):
		number += int(my_input("Enter a number: "))
	print("The total is %d." % number)


