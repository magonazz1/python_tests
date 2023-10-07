#!/usr/bin/python3
'''
' Author: Martin Magonagona
'
' Higher Level Programming
'
'''
'''
' this is a program that will be recommending what you should
' do based off of age you enter into the prompt.
'''
#asking the user to enter their age and convert it to integer

age = eval(input('\nPlease Enter Your Age: '))

#checking point

if (age < 5):
    print("\nYou are {} years old, Too young for anything\n".format(age))

elif (age == 5):
    print("\nYou are {} years old, Go to Kindergarten\n".format(age))

elif (age >= 6 and age < 17):
    print("\nYou are {} years old, Go to grade school "
    "(middle school)\n".format(age))

elif (age >= 17 and age < 27):
    print("\nYou are {} years old, Go to College\n".format(age))

elif not(age < 27):
    print("\nYou are {} years old, consider having a family if you "
    "don't already have one\n".format(age))

else:
    print("\nEnter a valid number please\n")
