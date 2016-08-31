#!/usr/bin/env python


from datetime import date


if __name__ == '__main__':
    year = date.today().year
    age = int(raw_input('What is your current age? '))
    retire_age = int(raw_input('At what age would you like to retire? '))
    left_year = retire_age - age

    output_string = 'You have ' + str( left_year ) + ' years left until you can retire.\n' + \
                    'It\'s ' + str( year ) + ', so you can retire in ' + str( year + left_year ) + '.'
    print output_string


