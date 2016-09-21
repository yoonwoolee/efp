#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import sys

my_input = input if sys.version_info >= (3,0) else raw_input

def validateNameFilled(name):
	if len(name) == 0:
		return False
	return True
def validateName(name):
	if len(name) < 2:
		return False
	return True


def validateZipCode(zip_code):
	return zip_code.isdigit()
def validateEmployeeID(employee_id):
	if len(employee_id) != 7:
		return False
	if employee_id[0].isalpha() and employee_id[1].isalpha() and employee_id[2] == '-' and employee_id[3:].isdigit():
		return True
	else:
		return False


def validateInput(first_name, last_name, zip_code, employee_id):
	ret_str = ""
	if validateName(first_name) == False:
		if validateNameFilled(first_name) == False:
			ret_str += 'The first name must be filled in.\n'
		else:
			ret_str += '"%s" is not a valid first name. It is too short.\n' % first_name
	if validateName(last_name) == False:
		if validateNameFilled(last_name) == False:
			ret_str += 'The last name must be filled in.\n'
		else:
			ret_str += '"%s" is not a valid last name. It is too short.\n' % last_name
	if validateZipCode(zip_code) == False:
		ret_str += 'The ZIP code must be numeric.\n'
	if validateEmployeeID(employee_id) == False:
		ret_str += '%s is not a valid ID.\n' % employee_id

	if len(ret_str) == 0:
		ret_str = 'There were no errors found.'
	return ret_str

if __name__ == "__main__":
	first_name = my_input("Enter the first name: ")
	last_name = my_input("Enter the last name: ")
	zip_code = my_input("Enter the ZIP code: ")
	employee_id = my_input("Enter an employee ID: ")
	print_str = validateInput(first_name, last_name, zip_code, employee_id)
	print(print_str)


