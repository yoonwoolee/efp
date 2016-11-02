#!/usr/bin/python

import requests
import sys
import json
import datetime

my_input = input if sys.version_info >= (3,0) else raw_input

url = 'https://test-38643.firebaseio.com/rest/saving-data/todo.json'

def request_todo_list():
	r = requests.get(url)
	if r.status_code / 100 != 2:
		print("error: requests error")
		sys.exit(1)
	todo_list_dic = r.json()
	if todo_list_dic is None:
		return []
	return todo_list_dic['data']

def print_todo_list(todo_list):
	if len(todo_list) == 0:
		print("empty !!\n\n")
	else:
		print("---------- ToDo list ---------")
		print("")
		for i, todo in enumerate(todo_list, 1):
			print("%d. %s"% (i, todo))
		print("")
		print("---------- ToDo list ---------")

def save_data(payload):
	r = requests.put(url,data=payload)
	if r.status_code / 100 != 2:
		print("error: requests error")
	else:
		print("success!")

def add_todo(todo_list, todo):
	todo_list.append(todo)
	payload = json.dumps({"data":todo_list})
	save_data(payload)

def del_todo(todo_list, num):
	todo_list.pop(num-1)
	payload = json.dumps({"data":todo_list})
	save_data(payload)

def main():
	while True:
		todo_list = request_todo_list()
		print_todo_list(todo_list)
		print('1. input new todo list')
		print('2. delete todo list')
		try:
			command_number = int(my_input('select command: '))
		except ValueError:
			print('bye')
			sys.exit(0)
		else:
			if command_number == 1:
				todo = my_input('Please input your todo: ')
				todo = todo.strip()
				if todo == '':
					continue
				add_todo(todo_list, todo)
			elif command_number == 2:
				try:
					del_num = int(my_input('please select del todo: '))
				except ValueError:
					print('please enter number')
					continue
				else:
					todo_count = len(todo_list)
					if todo_count < del_num or 0 >= del_num:
						continue
					del_todo(todo_list, del_num)
			else:
				print("bye")
				sys.exit(0)


if __name__ == "__main__":
	main()

	
