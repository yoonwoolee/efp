#!/usr/bin/env python



if __name__ == '__main__':

    width = input('width? ')
    height  = input('height? ')
    square = width * height

    PAINT_PER_ONE_LITER = 9
    paint_count = int (round( float( square ) / PAINT_PER_ONE_LITER ) )

    output_string = 'You will need to purchase ' + str( paint_count ) + ' liters of\n'
    output_string += 'paint to cover ' + str( square ) + ' square meters.'
    print output_string

