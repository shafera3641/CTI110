 # A Math Quiz Program
    # 11/29/22
    # CTI-110 P5HW2 - Math Quiz
    # Andrew Shafer
    #
import random

def display_intro():
    title = "A Math Quiz"
    print(title)

def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Exit"]
        
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
   
def display_separator():
    print("-" * 24)

def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 3 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input

def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result

def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Your Answer Is Correct.")
        return count
    
    elif user_solution > count:
        print("Too low, guess again")
        return user_solution
    elif user_solution < count:
        print("Too high, guess again")
        return user_solution

def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(-1, 21)
    if index == 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
   
def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 3:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)

main()