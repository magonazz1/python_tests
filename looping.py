#!/usr/bin/python3

'''
' Author: Martin Magonagona
'
' Higher Level Programming
'
'''
'''
' this is a program that experiments with loops (basic stuff)
'
'''
# Prompt the user to enter a value and evaluate it

n = eval(input("\nEnter your desired value to loop through: "))

# Check if the entered value is greater than 0

if n > 0:
    # Loop through the range from 0 to n-1

    for i in range(n):
        if ((i % 2) == 0):
            print((i % 2) == 0)

        # Print the current sequence number and the entered value

            print("\nSequence '{}' = {} ".format(i, n))

