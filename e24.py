#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys

my_input = input if sys.version_info >= (3,0) else raw_input



def isAnagram(first_word, second_word):
	first_word_len = len(first_word)
	if first_word_len == 0 or first_word_len != len(second_word):
		return False
	
	for first in first_word:
		include_word = False
		for second in second_word:
			if first == second:
				include_word = True
		if include_word != True:
			return False
	return True

if __name__ == "__main__":
	print("Enter two strings and I'll tell you if they are anagrams: ")
	first_str = my_input("Enter the first string: ")
	second_str = my_input("Enter the second string: ")
	if isAnagram(first_str, second_str):
		print('"%s" and "%s" are anagrams.' % (first_str, second_str))
	else:
		print('"%s" and "%s" are not anagrams.' % (first_str, second_str))
	
