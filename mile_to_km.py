#!/usr/bin/python3

'''
'Author: Martin Magonagona
'
'Higher Level Programming
'
'Creating a simple miles to kilometers converter
'''

'''
'the user enters the miles to be converted
'the program will convert them
'and finally, the program will output the result with a precision of 2
'''

mile = int(input('\nEnter Miles to Convert: '))
km = (float(mile) * float(1.609344))

print("\n{} mile(s) equals {:.2f} kilometers\n".format(mile, km))
