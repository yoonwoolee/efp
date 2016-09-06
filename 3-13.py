#!/usr/bin/env python




if __name__ == '__main__':
    principal = input('What is the principal amount? ')
    rate = input('What is the rate: ')
    number_of_years = input('What is the number of years: ')
    number_of_times = input('What is the number of times the interest\nis compounded per year: ')

    money = principal * ( 1 + (rate /100.0) / number_of_times) ** ( number_of_times * number_of_years )
    output_string = '$' + str(principal) + ' invested at ' + str(rate)
    output_string += '% for ' + str(number_of_years) + ' years compounded '
    output_string += str(number_of_times) +' times per year is $' + str(round(money,2))
    print output_string


