#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import sys
import random

my_input = input if sys.version_info >= (3,0) else raw_input


class Game:

	def init(self):
		self.value = 0
		self.input_count = 0
		self.msg = ""

	def init_game(self):
		while True:
			try:
				level = int(my_input("Pick a difficulty level (1, 2, or 3): "))
			except:
				continue
			else:
				if level < 1 or level > 3:
					continue
				break
		if level == 1:
			upper_range = 10 
		elif level == 2:
			upper_range = 100
		elif level == 3:
			upper_range = 1000

		self.value = random.randint(1, upper_range)
		self.input_count = 0
		self.msg = "I have my number. What\'s your guess? "

	def input_answer(self):
		while True:
			try:
				self.input_count += 1
				answer = int(my_input(self.msg))
			except:
				continue
			else:
				break
		return answer

	def check_value(self, answer):
		if self.value == answer:
			print("You got it in %d guesses!" % self.input_count)
			return True
		elif self.value > answer:
			self.msg = "Too low. Guess again: "
		elif self.value < answer:
			self.msg = "Too high. Guess again: "
		return False
	def input_again(self):
		while True:
			again = my_input("Play again? (y or n)")
			if again != "y" and again != "n":
				continue
			else:
				break
		return again

if __name__ == "__main__":
	game = Game()
	game.init_game()
	while True:
		answer = game.input_answer()
		if game.check_value(answer) == True:
			if game.input_again() == "y":
				game.init_game()
				continue
			else:
				break
		

