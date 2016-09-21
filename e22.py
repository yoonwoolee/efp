#!/usr/bin/python

import sys
my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	biggest  = -99999999
	input_numbers = []
	while True:
		try:
			input_numbers.append( int(my_input("Enter the first number: ")))
			input_numbers.append( int(my_input("Enter the second number: ")))
			input_numbers.append( int(my_input("Enter the third number: ")))
		except:
			input_numbers = []
			continue
		else:
			break
		
	for input_number in input_numbers:
		if biggest < input_number:
			biggest = input_number
			
	print("The largest number is %d." % biggest)



