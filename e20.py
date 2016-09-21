#!/usr/bin/python

import sys
my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	state_tax = 0.055
	county_tax = 0.0

	while True:
		try:
			amount = float(my_input("What is the order amount? "))
		except:
			continue
		else:
			break

	state = my_input("What state do you live in? ")

	if state == "Wisconsin":
		county = my_input("What county do you live in? ")
		if county == "Eau Claire":
			county_tax = 0.005
		elif county == "Dunn":
			county_tax = 0.004
	elif state == "Illinois":
		state_tax = 0.08


	state_tax_money = round(amount * state_tax, 2)
	print_str = "The state tax is $%.2f.\n" % state_tax_money
	if county_tax != 0.0:
		county_tax_money = round(amount * county_tax, 2)
		total_tax_money = state_tax_money + county_tax_money
		print_str += "The county tax is $%.2f.\n" % county_tax_money 
		print_str += "The total tax is $%.2f.\n" % total_tax_money
		print_str += "The total is $%.2f." % (amount + total_tax_money)
	else:
		print_str += "The total is $%.2f." % (amount + state_tax_money)


	print(print_str)
