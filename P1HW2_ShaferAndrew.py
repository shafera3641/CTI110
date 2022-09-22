Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# This program will calculate travel expenses
# 9/22/2022
# CTI-110 P1HW2 - Travel Expense
# Andrew Shafer
#

print('This program calculates and displays travel expenses')

budget = 1200
print('Enter Budget:', budget)

travel = 'Asheville'
print('Enter your travel destination:', travel)

gas = 250
print('How much do you think you will spend on gas?', gas)

hotel = 300
print('Approximately, how much will you need for accomodation/hotel?', hotel)

food = 200
print('Last, how much do you need for food?', food)

print('------------Travel Expenses------------')

variable = int(gas)+int(hotel)+int(food)

balance = int(budget)-int(variable)
print('Location:', travel)
print('Initial Budget:', budget)

print('Fuel:', gas)
print('Accomadation:', hotel)
print('Food:', food)

print('Remaining Balance:', balance)
