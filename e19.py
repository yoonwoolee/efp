#!/usr/bin/python


import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	while True:
		try:
			inch = 	float(my_input("what is your height?(inch) "))
		except:
			continue
		else:
			break

	while True:
		try:
			pound = float(my_input("what is your weight?(pound) "))
		except:
			continue
		else:
			break
	
	bmi = ( pound / (inch * inch)) * 703

	print("your BMI is %.1f." % bmi )
	if bmi >= 18.5 and bmi <= 25:
		print("You are within the ideal weight range.")
	else:
		print("You are overweight. You should see your doctor.")

