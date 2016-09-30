#!/usr/bin/python

import sys
import random

def my_input(input_msg):
	if sys.version_info >= (3,0):
		return input(input_msg)
	else:
		return raw_input(input_msg)


def cal_sum(numbers):
	s = 0
	for number in numbers:
		s += number
	return s
def cal_avg(numbers):
	s = cal_sum(numbers)
	return s / len(numbers)
	
def cal_min(numbers):
	min_value = sys.maxsize
	for number in numbers:
		if number < min_value:
			min_value = number
	return min_value

def cal_max(numbers):
	max_value = -(sys.maxsize)
	for number in numbers:
		if number > max_value:
			max_value = number
	return max_value
	
def cal_std_dev(numbers):
	avg = cal_avg(numbers)
	s = 0
	for number in numbers:
		s += ((number - avg) ** 2)
	return (s*1.0 / len(numbers)) ** 0.5
def print_numbers(numbers):
	print_str = "Numbers: "
	numbers_str = map(str, numbers)
	print_str += ', '.join(numbers_str)
	print(print_str)


if __name__ == "__main__":
	numbers = []

	while True:

		input_value = my_input("Enter a number: ")
		if input_value == "done":
			break
		try:
			number = int(input_value)
		except ValueError:
			continue
		else:
			numbers.append(number)

	numbers_len = len(numbers)
	
	if numbers_len != 0:
		print_numbers(numbers)
		avg_v = cal_avg(numbers)
		min_v = cal_min(numbers)
		max_v = cal_max(numbers)
		std_dev_v = cal_std_dev(numbers)
		print("The average is %d." % avg_v)
		print("The minimum is %d." % min_v)
		print("The maximum is %d." % max_v)
		print("The standard deviation is %.2f." % std_dev_v)



