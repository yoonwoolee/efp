#!/usr/bin/python

import sys
from operator import itemgetter

def my_input(input_msg):
	if sys.version_info >= (3,0):
		return input(input_msg)
	else:
		return raw_input(input_msg)

def print_data(data):
	print("name\t\t\t | Position\t\t\t | Separation Date") 
	print("------------------------------------------------------------------")
	for d in data:
		print("%s %s\t\t | %s\t\t | %s\t\t" % (d['First Name'], d['Last Name'], d['Position'], d['Separation date']))


if __name__ == "__main__":
	data = [{'First Name': 'John', 'Last Name': 'Johnson','Position': 'Manager','Separation date': '2016-12-31'},
		{'First Name': 'Tou', 'Last Name': 'Xiong','Position': 'Software Engineer','Separation date': '2016-10-15'},
		{'First Name': 'Michaela', 'Last Name': 'Michaelson','Position': 'District Manager','Separation date': '2015-12-19'},
		{'First Name': 'Jake', 'Last Name': 'Jacobson','Position': 'Programmer' ,'Separation date': ''},
		{'First Name': 'Jacquelyn', 'Last Name': 'Jackson','Position': 'DBA','Separation date': ''},
		{'First Name': 'Sally', 'Last Name': 'Weber', 'Position': 'Web Developer', 'Separation date': '2015-12-18'}]

	data = sorted(data, key=itemgetter('Last Name')) 
	print_data(data)


