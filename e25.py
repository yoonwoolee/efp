#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys

my_input = input if sys.version_info >= (3,0) else raw_input

NORMAL = 0
VERY_WEAK = 1
WEAK = 2
STRONG = 3
VERY_STRONG = 4

def passwordValidator(password):
	only_number = password.isdigit()
	only_alpha = password.isalpha()
	short_word = False

	if len(password) < 8:
		short_word = True

	if only_number == True and short_word == True:
		return VERY_WEAK

	if only_alpha == True and short_word == True:
		return WEAK

	special_char = False
	for p in password:
		if p.isalpha() == False and p.isdigit() == False:
			special_char = True

	if only_alpha == False and only_number == False and short_word == False:
		if special_char == True:
			return VERY_STRONG 
		else:
			return STRONG

	return NORMAL

if __name__ == "__main__":
	password = my_input("input password: ")
	power = passwordValidator(password)
	switcher = {
		NORMAL: 'normal',
		VERY_WEAK: 'very weak',
		WEAK: 'weak',
		STRONG: 'strong',
		VERY_STRONG: 'very strong'
	}
	power_str = switcher.get(power, '')
	print_str = "The password '%s' is a %s password." % (password, power_str)
	print(print_str)


