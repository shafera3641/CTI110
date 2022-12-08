# CTI-110
# P4HW1 - Score List
# Andrew Shafer
# 12/1/22
#


# Asks the user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Creates an empty list to store the scores
scores = []

# Creates a loop to collect the scores from the user
while len(scores) < num_scores:
    score = float(input("Enter a score: "))

    # Checks if the score is valid (between 0 and 100)
    if 0 <= score <= 100:
        scores.append(score)
    else:
        print("Invalid Score entered!!!! Score should be between 0 and 100")

# Calculates the lowest score
lowest = min(scores)

# Removes the lowest score from the list
scores.remove(lowest)

# Calculates the average of the remaining scores
average = sum(scores) / len(scores)

# Determine the letter grade for the average
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print the results
print("------------Results------------")
print("Lowest score:", lowest)
print("Modified List:", scores)
print(f"Scores Average: {average:.2f}")
print("Letter grade:", letter_grade)
print("------------------------------")