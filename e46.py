#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os
from operator import itemgetter




def str_star(count):
	return ''.join(['*' for _ in range(count)])

if __name__ == "__main__":
	with open("input_data_e46","r") as f:
		input_data = f.read()
		word_list = input_data.split(" ")
		word_list = [word.strip() for word in word_list]
	key_word_list = []
	for word in word_list:
		bexist = False
		for key_word in key_word_list:
			if key_word['word'] == word:
				bexist = True
				break
		if bexist == False:
			key_word_list.append({'word':word, 'count':0})
	
	for key_word in key_word_list:
		for word in word_list:
			if key_word['word'] == word:
				key_word['count']+=1
	key_word_list = sorted(key_word_list, key=itemgetter('count'))
	key_word_list = key_word_list[-1::-1]

	for key_word in key_word_list:
		print("%s: %s" % (key_word['word'],str_star(key_word['count'])))
