# Initialize variables
employees = 0
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0

# Ask the user to enter an employee name or 'None' to terminate the program
name = input("Enter the employee's name or 'None' to terminate: ")

# Loop until the user enters 'None'
while name != 'None':
    # Ask the user to enter the number of hours the employee worked
    hours_worked = float(input("How many hours did they work? "))

    # Ask the user to enter the employee's pay rate
    pay_rate = float(input("What is the employee's pay rate? "))

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

    # Add the overtime pay and regular pay amounts to the totals
    overtime_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay

    # Increment the employee count
    employees += 1

    # Ask the user to enter another employee name or 'None' to terminate the program
name = input("Enter the employee's name or 'None' to terminate: ")

# Display the results
print("-----------------------------------")
print("Total number of employees entered:", employees)
print("Total amount payed for overtime: $" + str(overtime_total))
print("Total amount payed for regular hours: $" + str(regular_pay_total))
print("Total amount payed in gross: $" + str(gross_pay_total))