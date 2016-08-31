#!/usr/bin/env python


from datetime import date


if __name__ == '__main__':

    TAX = 0.055
    iter_num = [1,2,3]
    input_data = []
    for num in iter_num:
        price = input('Price of item %d: ' % num )
        quantity = input('Quantity of item %d: ' % num)
        input_data.append( { 'p' : price , 'q' : quantity } )

    subtotal = 0
    for d in input_data:
        subtotal += d['p'] * d['q']

    tax = subtotal * TAX
    total = tax + subtotal

    output_string = 'Subtotal: $%s \n' % round( subtotal , 2 )
    output_string += 'Tax: $%s \n' % round( tax , 2 )
    output_string += 'Total: $%s \n' % round( total , 2 )
    print output_string


