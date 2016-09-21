#!/usr/bin/python

import sys

my_input = input if sys.version_info >= (3,0) else raw_input


if __name__ == "__main__":
	input_str = "press C to convert from Fahrenheit to Celsius.\n"
	input_str += "Press F to convert from Celsius to Fahrenheit.\n"
	input_str += "Your choice: "
	input_str2 = "Please enter the temperature in "
	output_str = "The temperature in "

	mode = my_input(input_str)
	if mode == 'c' or mode == 'C':
		input_str2 += "Fahrenheit: "
		while True:
			try:
				F = int(my_input(input_str2))
			except:
				continue
			else:
				break

		C = (F - 32) * 5.0/7
		output_str += "Celsius is %d." % C
	elif mode == 'f' or mode == 'F':
		input_str2 += "Celsius: "
		while True:
			try:
				C = int(my_input(input_str2))
			except:
				continue
			else:
				break
		F = ( C * 9.0 / 5) + 32
		output_str += "Fahrenheit is %d." % F
	else:
		output_str = "mode error"
	print(output_str)

