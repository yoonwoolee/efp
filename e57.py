#!/usr/bin/python

import sys
import random

my_input = input if sys.version_info >= (3,0) else raw_input

CSV_FILENAME = 'e57_problem.csv'

def make_row(line):
	data = line.split(',')
	q = data[0].strip(' \n')
	try:
		c = int(data[1])
		ra = int(data[2])-1
	except ValueError:
		print('Value error: must be number')
		sys.exit(1)
	else:
		a = [ {'a': data[3+r].strip(' \n'),'ra':False } for r in range(c) ]
		a[ra]['ra'] = True
		random.shuffle(a)
		return {'q': q,'a':a}

def load_problem():
	with open(CSV_FILENAME) as f:
		return map(make_row,f)

def process_quiz(data,correct_count):
	while True:
		try:
			print('correct answer count: %d' % correct_count)
			print(data['q'])
			for n, answer in enumerate(data['a'],1):
				print("%d. %s" % (n, answer['a']))
			input_answer = int(my_input(': '))
		except ValueError:
			continue
		else:
			if input_answer < 1 and input_answer > len(data['a']):
				continue
			if True == data['a'][input_answer-1]['ra']:
				print("correct")
				return True
			else:
				print("wrong")
				return False

def main():
	datas = load_problem()
	random.shuffle(datas)
	correct_count = 0
	for data in datas:
		if True == process_quiz(data,correct_count):
			correct_count +=1
		else:
			break
	print("bye")

if __name__ == "__main__":
	main()
