#!/usr/bin/env python




if __name__ == '__main__':
    principal = input('Enter the principal: ')
    rate_of_interest = input('Enter the rate of interest: ')
    number_of_years = input('Enter the number of years: ')

    money = principal * ( 1 + (rate_of_interest /100.0)  * number_of_years )


    output_string = 'After ' + str(number_of_years) + ' years at ' + str(rate_of_interest)
    output_string += '%, the investment will be worth $' +  str(int(money))
    print output_string


