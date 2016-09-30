#!/usr/bin/python

import sys
import random
import string

def my_input(input_msg):
	if sys.version_info >= (3,0):
		return input(input_msg)
	else:
		return raw_input(input_msg)


if __name__ == "__main__":
	try:
		min_length = int(my_input("What's the minimum length? "))
		sel_length = min_length + random.randint(0, 4)
		special_char_count = int(my_input("How many special characters? "))
		number_count = int(my_input("How many numbers? "))
		normal_length  = sel_length - (special_char_count + number_count)
	except ValueError:
		print("you must input number")
		sys.exit(1)
	else:
		if min_length <= 0:
			print("length error")
			sys.exit(1)
		if special_char_count < 0:
			print("special char count error")
			sys.exit(1)
		if number_count < 0:
			print("number count error")
			sys.exit(1)

		if normal_length < 0:
			print("specail and number count is too many error")
			sys.exit(1)
	output = []

	for _ in range(sel_length):
		output.append(None)

	for _ in range(sel_length):
		if special_char_count > 0 and number_count > 0:
			if random.randint(0, 1) == 0:
				special_char_count -= 1
				sel_char = random.choice(string.punctuation)
			else:
				number_count -= 1
				sel_char = random.choice(string.digits)
		elif special_char_count > 0:
			special_char_count -= 1
			sel_char = random.choice(string.punctuation)
		elif number_count > 0:
			number_count -= 1
			sel_char = random.choice(string.digits)
		else:
			sel_char = random.choice(string.ascii_letters)

		while True:
			sel_index = random.randint(0, sel_length - 1)
			if output[sel_index] == None:
				break
		output[sel_index] =  sel_char

	print("Your password is ")
	print("".join(output))

