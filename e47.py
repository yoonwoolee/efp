#!/usr/bin/python

import requests
import sys


if __name__ == "__main__":
	r = requests.get('http://api.open-notify.org/astros.json')
	if r.status_code /100 != 2:
		print("error: requests error")
		sys.exit(1)	
	json_data = r.json()
	peoples = json_data['people']

	print("name                 | craft     ")
	print("---------------------|-----------")
	for people in peoples:
		print("%s     | %s " % (people['name'],people['craft']))
	
