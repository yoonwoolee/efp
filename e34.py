#!/usr/bin/python

import sys

def my_input(input_msg):
	if sys.version_info >= (3,0):
		return input(input_msg)
	else:
		return raw_input(input_msg)

def print_employees(employees):
	print("There are %d employees:" % len(employees))
	for employee in employees:
		print(employee)

def remove_employees(employees, target_name):
	for i, name in enumerate(employees):
		if name == target_name:
			del employees[i]

if __name__ == "__main__":
	employees = ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]
	print_employees(employees)
	name = my_input("Enter an employee name to remove: ")
	remove_employees(employees, name)
	print_employees(employees)


