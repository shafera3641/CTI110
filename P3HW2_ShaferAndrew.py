# CTI-110
# P3HW2 - Salary
# Andrew Shafer
# 12/1/22
#

# Ask the user to enter the employee's name
name = input("Enter the employee's name: ")

# Ask the user to enter the number of hours the employee worked
hours_worked = float(input("Enter number of hours worked: "))

# Ask the user to enter the employee's pay rate
pay_rate = float(input("Enter the employee's pay rate: "))

# Calculate the amount of overtime hours the employee worked
overtime_hours = 0
if hours_worked > 40:
    overtime_hours = hours_worked - 40

# Calculate the amount of overtime pay the employee is owed
overtime_pay = overtime_hours * pay_rate * 1.5

# Calculate the amount of regular pay the employee is owed
regular_pay = hours_worked * pay_rate

# Calculate the employee's gross pay (total amount to be paid)
gross_pay = regular_pay + overtime_pay

# Display the results
print("-----------------------------------")
print("Employee name:", name)
print("")
print("Hours Worked     Pay Rate     OverTime     OverTime Pay     RegHour Pay     Gross Pay")
print("------------------------------------------------------------------------------------------")
print(f'{hours_worked:<17.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<13.2f}')
