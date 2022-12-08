# This program will calculate travel expenses
# 9/22/2022
# CTI-110 P1HW2 - Travel Expense
# Andrew Shafer
#

#Displays a title
print('---This Program Calculates And Displays Travel Expenses---')

#Asks the user for their budget
budget =float(input("Please enter your budget: "))

#Asks the user for their travel destination
travel = input("Enter your travel destination: ")

#Asks the user thier gas cost
gas = float(input("How much do you think you will spend on gas?"))

#Asks the user how much their accomodation is
hotel = float(input("Approximately, how much will you need for accomodation/hotel?"))

#Gets input for food
food = float(input("Last, how much do you need for food?"))

print('------------Travel Expenses------------')

#Calculates the remaining balance
variable = int(gas)+int(hotel)+int(food)

balance = int(budget)-int(variable)
#Displays the results
print('Location:', travel)
print('Initial Budget:', budget)
print('Fuel:', gas)
print('Accomadation:', hotel)
print('Food:', food)
print('Remaining Balance:', float(balance))
