#!/usr/bin/python

import sys

my_input = input if sys.version_info >= (3,0) else raw_input



if __name__ == "__main__":

	username = my_input("What is the username: ")
	password = my_input("What is the password: ")

	if username == "ywlee" and password == "abc$123":
		print("Welcome!")
	else:
		print("That password is incorrect.")

