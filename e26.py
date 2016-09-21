#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import sys

my_input = input if sys.version_info >= (3,0) else raw_input


def calculateMonthsUntilPaidOff(balance, apr_percent, payment):
	i = apr_percent / 365.0
	return  -(1.0/30.0) * (math.log(1 + (balance / payment) * (1 + ((1 + i) ** 30))) / math.log(1+i))


if __name__ == "__main__":
	while True:
		try:
			balance = float(my_input("What is your balance? "))
			apr_percent = float(my_input("What is the APR on the card (as a percent)? "))
			payment = float(my_input("What is the monthly payment you can make? "))
		except:
			continue
		else:
			break

	month = calculateMonthsUntilPaidOff(balance, apr_percent, payment)
	print_str = "It will take you %d months to pay off this card" % month

	print(print_str)

