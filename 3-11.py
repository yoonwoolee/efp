#!/usr/bin/env python


if __name__ == '__main__':
    euro = input("How many Euros are you exchanging? ")
    exchange_rate = input("What is the exchange rate? ")

    dollar = euro * exchange_rate / 100
    output_string = str(euro) + ' Euros at an exchange rate of ' + str(exchange_rate) + ' is\n'
    output_string += str( round(dollar,2) ) + ' dollars'
    print output_string


