#!/usr/bin/env python


if __name__ == '__main__':
    a_str = raw_input('What is the first number ? ')
    b_str = raw_input('What is the second number ? ')
    a_int = int(a_str)
    b_int = int(b_str)

    output_string = a_str + ' + ' + b_str + ' = ' + str(a_int + b_int) + '\n' + \
                    a_str + ' - ' + b_str + ' = ' + str(a_int - b_int) + '\n' + \
                    a_str + ' * ' + b_str + ' = ' + str(a_int * b_int) + '\n' + \
                    a_str + ' / ' + b_str + ' = ' + str(a_int / b_int)
    print output_string

