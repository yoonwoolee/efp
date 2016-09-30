#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os
import json

def my_input(msg):
	return input(msg) if sys.version_info >= (3,0) else raw_input(msg)

def parse_product_data(json_filename):
	with open(json_filename, "r") as f:
		return json.loads(f.read())['products']

if __name__ == "__main__":
	products  = parse_product_data("product.json")

	while True:
		product_name = my_input("What is the product name? ")

		out = [ product  for product in products if product['name'] == product_name]
		if len(out) != 0:
			product = out[0]
			print("Name: %s" % product['name'])
			print("Price: %s" % product['price'])
			print("Quantity on hand: %s" % product['quantity'])
			break
		print("Sorry, that product was not found in our inventory.")

