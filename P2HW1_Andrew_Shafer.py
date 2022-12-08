# This program will calculate travel expenses
# 9/22/2022
# CTI-110 P2HW1 - Travel
# Andrew Shafer
#

#Displays a title
print('---This Program Calculates And Displays Travel Expenses---')

#Asks the user for their budget
budget = input("Please enter your budget: ")

#Asks the user for their travel destination
travel = input("Enter your travel destination: ")

#Asks the user thier gas cost
gas = input("How much do you think you will spend on gas?")

#Asks the user how much their accomodation is
hotel = input("Approximately, how much will you need for accomodation/hotel?")

#Gets input for food
food = input("Last, how much do you need for food?")

print('------------Travel Expenses------------')

#Calculates the remaining balance
variable = int(gas)+int(hotel)+int(food)

balance = int(budget)-int(variable)

#Displays the results as a float
initialBudget = float(budget)

Fuel = float(gas)

Accommodation = float(hotel)

Food = float(food)

remainingBalance = float(balance)

#Displays the results with correct positioning 
right_aligned_string = "Location:".ljust(18)
print(right_aligned_string, travel)

#Includes a dollar sign infront of its number
formatted_string = "Initial Budget:    ${:.2f}".format(initialBudget)
right_aligned_string = formatted_string.ljust(20)
print(right_aligned_string)

formatted_string = "Fuel:              ${:.2f}".format(Fuel)
right_aligned_string = formatted_string.ljust(29)
print(right_aligned_string)

formatted_string = "Accommodation:     ${:.2f}".format(Accommodation)
right_aligned_string = formatted_string.ljust(20)
print(right_aligned_string)

formatted_string = "Food:              ${:.2f}".format(Food)
right_aligned_string = formatted_string.ljust(20)
print(right_aligned_string)
print("---------------------------------------")
formatted_string = "Remaining Balance: ${:.2f}".format(remainingBalance)
right_aligned_string = formatted_string.ljust(20)
print(right_aligned_string)
