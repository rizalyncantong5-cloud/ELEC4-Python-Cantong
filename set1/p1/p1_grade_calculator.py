
# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 17, 2026

# Global variable for storing the grades
grade_list = []


# Function 1: Get grades from the user
def input_grades():
    entered_grades = []

    while True:
        try:
            total = int(input("How many grades do you want to enter? "))

            if total > 0:
                break

            print("Please enter at least 1 grade.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    for number in range(1, total + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {number}: "))

                if 0 <= grade <= 100:
                    entered_grades.append(grade)
                    break

                print("Grade must be from 0 to 100.")

            except ValueError:
                print("Invalid grade. Please enter a number.")

    return entered_grades


# Function 2: Calculate the average
def find_average(scores):
    return sum(scores) / len(scores)


# Function 3: Find the highest grade
def find_highest(scores):
    highest = max(scores)
    return highest


# Function 4: Find the lowest grade
def find_lowest(scores):
    lowest = min(scores)
    return lowest


# Function 5: Check the student's result
def check_result(scores):
    average = find_average(scores)

    if average >= 75:
        return "PASSED"

    return "FAILED"


# Function 6: Show the complete results
def show_results(scores):
    average = round(find_average(scores), 2)
    highest = find_highest(scores)
    lowest = find_lowest(scores)
    result = check_result(scores)

    print("\n========== GRADE SUMMARY ==========")
    print(f"Entered Grades : {scores}")
    print(f"General Average: {average}")
    print(f"Highest Grade  : {highest}")
    print(f"Lowest Grade   : {lowest}")
    print(f"Final Result   : {result}")
    print("===================================")

# Main program
while True:
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("1. Enter Grades")
    print("2. Display Results")
    print("3. Exit")

    selected_option = input("Choose an option: ")

    if selected_option == "1":
        grade_list = input_grades()
        print("\nGrades have been saved successfully!")

        show_results(grade_list)

    elif selected_option == "2":
        if grade_list:
            show_results(grade_list)
        else:
            print("\nNo grades found. Enter grades first.")

    elif selected_option == "3":
        print("Program closed. Thank you!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")


# LOCAL AND GLOBAL VARIABLES:
# A global variable is declared outside a function and can be accessed in different parts of the program.
# In this program, grade_list is the global variable used to store the student's grades.
# A local variable is declared inside a function and is only available within that function.
# For example, entered_grades is local to input_grades() and stores the grades before returning them.
