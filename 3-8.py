#!/usr/bin/env python



if __name__ == '__main__':

    people = input('How many people? ')
    pizza  = input('How many pizzas do you have? ')

    pieces = input('How many pieces are in a pizza? ')

    all_pieces = pizza * pieces
    left_pieces = all_pieces % people
    people_pieces = all_pieces / people

    output_string = str( people ) + ' people with ' + str( pizza ) + ' pizzas\n'
    output_string += 'Each person gets ' + str( people_pieces ) + ' pieces of pizza.\n'
    output_string += 'There are ' + str( left_pieces ) + ' leftover pieces.'
    print output_string

