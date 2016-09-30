#!/usr/bin/python

import sys
import random

def my_input(input_msg):
	if sys.version_info >= (3,0):
		return input(input_msg)
	else:
		return raw_input(input_msg)


if __name__ == "__main__":
	
	answers = ["Yes", "No", "Maybe", "Ask again later"]
	my_input("What's your question? ")
	answer_index = random.randint(0, len(answers) - 1)

	print(answers[answer_index])

