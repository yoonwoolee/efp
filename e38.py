#!/usr/bin/python

import sys

def my_input(input_msg):
	if sys.version_info >= (3,0):
		return input(input_msg)
	else:
		return raw_input(input_msg)

def filterEvenNumbers(numbers):
	new_numbers  = [] 
	for n in numbers:
		if n % 2 == 0:
			new_numbers.append(n)
	return new_numbers

if __name__ == "__main__":
	try:
		numbers = map(int , my_input("Enter a list of numbers, separated by spaces: ").split())
	except ValueError:
		print("Please input only number value. ")
		sys.exit(1)
	else:
		numbers = filterEvenNumbers(numbers)
		if len(numbers) == 0:
			print("The even numbers is not exist")
		else:
			print("The even numbers are %s." % ' '.join(map(str,numbers)))


