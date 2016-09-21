#!/usr/bin/python

import sys

my_input = input if sys.version_info >= (3,0) else raw_input



if __name__ == "__main__":

	while True:
		try:
			weight = float(my_input("What is your weight? "))
		except:
			continue
		else:
			break
	while True:
		gender = my_input("What is your gender? (man or woman) ")
		if gender == 'man' or gender == 'woman':
			break
	while True:
		try:
			amount = float(my_input("What is your amount? "))
		except:
			continue
		else:
			break

	while True:
		try:
			past_time = int(my_input("What is your past time after drinking? "))
		except:
			continue
		else:
			break
	if gender == "man":
		r = 0.73
	else:
		r = 0.6

	BAC = amount * 5.14 / weight * r - 0.015 * past_time
	print_str = "Your BAC is %.2f\n" % BAC
	if BAC < 0.08:
		print_str += "It is legal for you to drive."
	else:
		print_str += "It is not legal for you to drive."
	print(print_str)
