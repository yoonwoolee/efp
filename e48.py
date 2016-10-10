#!/usr/bin/python

import requests
import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	try:
		with open("key") as f:
			key = f.read()
			key = key.strip('\n')
	except:
		print("error: can't read key value")
		sys.exit(1)
	
	input_value = my_input("Where are you? ")
	city = input_value.split()
	if len(city) == 2:
		city_str = '%s,%s' % (city[0], city[1])
	else:
		city_str = '%s' % city[0]
	
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s&units=Imperial' % (city_str, key))
	if r.status_code /100 != 2:
		print("error: requests error")
		sys.exit(1)	

	json_data = r.json()
	print("%s weather:\n%s degrees Fahrenheit" % (city[0],json_data['main']['temp']))
