#!/usr/bin/python

import sys
my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	switcher = {
		1: "January",
		2: "Febuary",
		3: "March",
		4: "April",
		5: "May",
		6: "June",
		7: "July",
		8: "August",
		9: "September",
		10: "October",
		11: "November",
		12: "December"
	}
	while True:
		try:
			number_mon = int(my_input("Please enter the number of the month: "))
		except:
			continue
		else:
			break

	if number_mon < 1 or number_mon > 12:
		print_str = "input error "
	else:
		str_mon = switcher.get(number_mon,"")
		print_str = "The name of the month is %s." % str_mon
	print(print_str)

