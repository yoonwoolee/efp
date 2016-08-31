#!/usr/bin/env python



if __name__ == '__main__':

    length = input('What is the length of the room in feet? ')
    width  = input('What is the width of the room in feet? ')
    feet = length * width
    FEET_TO_METER = 0.09290304
    meter = feet * FEET_TO_METER

    output_string = 'You entered dimensions of ' + str(length) + ' feet by ' + str(width) + ' feet\n'
    output_string += 'The area is\n'
    output_string += str(feet) + ' square feet\n'
    output_string += str( round( meter , 3 ) ) + ' square meters'
    print output_string

