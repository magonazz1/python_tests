#!/usr/bin/python3
import sys
'''
' Author: Martin Magonagona
' Program Name: Investment Simulator
' Language: Python
'''
'''
' Description: This program asks the user to input an amount they wish to invest
'               and it follows up with them having to also input the interest
'               rate expected for their investment to earn per year, and then
'               the program performs the calculation over a span of 10 years
'               and then prints out (1) Initial Investment (2) Rate applied
'               (3) Total Interest amount earned (4) Total Investment Return.
'''
'''
' Program Execution:
' 
' The Program will first begin with a little information about what it does, and
' the user will be provided with some options to choose from, and perform the task
'''
#Calculations
#Error Handling Function
_error = 0

def input_error():
    global _error
    _error = input("\nInvalid Selection: press 'Enter' to try again\n")

#ask the user to choose interest type (Compound Interest) or (simple Interest)
intro = input("\nWelcome to Investment Simulator\n\nThis program what it does is basically "
        "calculate how big can your investment\ngrow over a period of 10 years using"
        " your desired interest rate and type.\n\nPlease, press 'enter' to proceed")

valid_choices = [1, 2]

while True:
        interest_type = (input("\nChoose the interest type to work with\n\n"
            "Press (1) For: 'Compound Interest'    "
            "Press (2) For: 'Simple Interest'\nPrompt: "))

        if (interest_type.isdigit()):
                interest_type = int(interest_type)

                if (interest_type in valid_choices):
                    proceed_calc()

        input_error()
