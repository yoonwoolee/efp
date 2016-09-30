#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys


def parse_sal_data(csv_filename):
	sal_data = []
	with open(csv_filename, "r") as f:
		for line in f:
			line_data = line.split(',')
			sal_data.append({'Last': line_data[0].strip(), 'First': line_data[1].strip(), 'Salary': line_data[2].replace('\n','').strip()})
	return sal_data

def dup_str(input_str, num):
	return ''.join([input_str for _ in range(num)]) 

def make_row(col1, col1_space, col2, col2_space, col3, col3_space):
	return col1 + dup_str(' ', col1_space - len(col1)) + col2 + dup_str(' ', col2_space - len(col2)) + col3 + dup_str(' ', col3_space - len(col3))

def print_sal_data(sal_data):
	lastname_max_len = max(map(lambda sal_item:len(sal_item['Last']), sal_data))
	firstname_max_len = max(map(lambda sal_item:len(sal_item['First']), sal_data))
	salary_max_len = max(map(lambda sal_item:len(sal_item['Salary']), sal_data))

	out_string = make_row('Last', lastname_max_len+1, 'First', firstname_max_len+1, 'Salary', salary_max_len+1)
	out_string += '\n' + dup_str('-',len(out_string)) + '\n'
	for sal_item in sal_data:
		out_string += make_row(sal_item['Last'], lastname_max_len+1, sal_item['First'], firstname_max_len+1, sal_item['Salary'], salary_max_len+1) + '\n'
	print(out_string)

if __name__ == "__main__":
	sal_data = parse_sal_data("input_data.csv")
	print_sal_data(sal_data)

