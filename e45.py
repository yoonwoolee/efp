#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os

def my_input(msg):
	return input(msg) if sys.version_info >= (3,0) else raw_input(msg)


if __name__ == "__main__":
	out_filename = my_input("What is stored filename? ")
	with open("input_data_e45","r") as f:
		input_data = f.read()
		input_data = input_data.replace("utilize","use")
	with open(out_filename,"w") as f:
		f.write(input_data)
