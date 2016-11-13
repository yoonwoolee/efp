#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import sys
import multiprocessing

my_input = input if sys.version_info >= (3,0) else raw_input

def multi(arg):
	x, yy = arg
	return ["%d x %d = %d" % (x, y, x * y) for y in range(yy)] 

def print_data(s):
	print(s)

if __name__ == "__main__":
	arg = ( (i,13) for i in range(13))
	pool = multiprocessing.Pool(processes=2)
	out_data = pool.map(multi,arg)
	map(print_data,out_data)

