#!/usr/bin/python

import requests
import sys
import json
import datetime

my_input = input if sys.version_info >= (3,0) else raw_input

JSON_FILENAME = 'e56_items.json'
CSV_FILENAME = 'e56_items.csv'
HTML_FILENAME = 'e56_items.html'

def make_html_row(item):
	return '<tr><td>' + item['name'] + '</td><td>' + item['serial'] + '</td><td>' + ('$%.2f' % item['value']) + '</td></tr>\n'
def save_HTML(items):
	with open(HTML_FILENAME,'w') as f:
		f.write('<html>\n')
		f.write('<body>\n')
		f.write('<table>\n')
		f.write('<tr><th>Name</th><th>Serial Number</th><th>Value</th></tr>\n')
		rows = map(make_html_row,items)
		map(f.write,rows)
		f.write('</table>\n')
		f.write('</body>\n')
		f.write('</html>\n')

def save_CSV(items):
	with open(CSV_FILENAME,'w') as f:
		for item in items:
			f.write(item['name'] +', ' + item['serial'] +', ' + ('$%.2f' % item['value'])+'\n')
def save_item_by_json(items):
	with open(JSON_FILENAME,'w') as f:
		f.write(json.dumps(items))

def load_item_by_json():
	try:
		with open(JSON_FILENAME) as f:
			return json.loads(f.read())
	except:
		return []
def input_item():
	name = my_input('input item name: ')
	serial = my_input('input serial number: ')
	try:
		value = int(my_input('input value: '))
	except ValueError:
		print('value error: please input number')
		exit(1)
	return name, serial, value

def main():
	items = load_item_by_json()
	while True:
		sel = my_input('1: add item\n2: report HTML\n3: report CSV : ')
		if sel == '1':
			name, serial, value = input_item()
			items.append({'name': name, 'serial': serial, 'value': value})
			save_item_by_json(items)
		elif sel == '2':
			save_HTML(items)
		elif sel == '3':
			save_CSV(items)
		else:
			print('bye')
			exit(1)

if __name__ == "__main__":
	main()
