#!/usr/bin/python

import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	while True:
		try:
			amount = float(my_input("What is the order amount? "))
		except:
			continue
		else:
			break

	state = my_input("What is the state? ")
	TAX = 0.055
	tax_value = amount * TAX
	total = amount + tax_value

	print_str = ""
	if state == "WI":
		print_str += "The subtotal is $%.2f\n" % round(amount,2)
		print_str += "The tax is $%.2f\n" % round(tax_value,2)
	print_str += "The total is $%.2f" % round(total,2)
	print(print_str)



