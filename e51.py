#!/usr/bin/python

import requests
import sys
import json
import datetime

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	url = 'https://test-38643.firebaseio.com/rest/saving-data/note.json'
	if len(sys.argv) < 2:
		print('arg count not enough')
		sys.exit(1)
	if sys.argv[1] == 'new':
		r=requests.get(url)
		if r.status_code / 100 !=2:
			print("error: requests error")
			sys.exit(1)
		data = r.json()
		if data is None:
			data = {"data":[]}
		memo_str = ' '.join(sys.argv[2:])
		date_str = str(datetime.date.today())
		message_str = date_str + ' - ' + memo_str
		data["data"].append(message_str)
		data_dump = json.dumps(data)
		payload = data_dump
		r = requests.put(url, data=payload)
		if r.status_code / 100 !=2:
			print("error: requests error")
		else:
			print("success!")

	elif sys.argv[1] == 'show':
		r = requests.get(url)
		if r.status_code / 100 != 2:
			print("error: requests error")
			sys.exit(1)
		data = r.json()
		if data is None:
			print("data is empty") 
		else:
			array = data['data']
			for v in array:
				print("%s"% (v))
	else:
		print('command error')




	
