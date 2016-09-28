#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":

	for i in range(13):
		for j in range(13):
			print("%d x %d = %d") % (i, j, i * j)

