# CTI-110
# P2HW2 - List
# Andrew Shafer
# 12/1/22
#

#Asks the user for the grade for each module
m1 = float(input("Enter grade for module 1: "))
m2 = float(input("Enter grade for module 2: "))
m3 = float(input("Enter grade for module 3: "))
m4 = float(input("Enter grade for module 4: "))
m5 = float(input("Enter grade for module 5: "))
m6 = float(input("Enter grade for module 6: "))
#List with descriptive name
grades = [m1, m2, m3, m4, m5, m6]


# Calculates the lowest grade in the list
lowest = min(grades)

# Calculates the highest grade in the list
highest = max(grades)

# Calculates the sum of all grades
sum = sum(grades)

# Calculates the average
average = sum/6
average = "{0:.2f}".format(average)
#Displays the results
print("------------Results------------")
print("Lowest Grade: ",lowest)
print("Highest Grade: ",highest)
print("Sum of Grades: ",sum)
print("Average: ",average)
print("-------------------------------")