
# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P2 - Main Program
# Date: November 17, 2026

# Import styles
import student_utils
from student_utils import get_average, get_status

# Built-in module
from datetime import datetime


# Ask the user for grades
grades = []

print("===== STUDENT UTILITIES PROGRAM =====")

while True:
    try:
        total = int(input("How many grades will you enter? "))

        if total > 0:
            break

        print("Please enter at least one grade.")

    except ValueError:
        print("Invalid input. Enter a whole number.")


for number in range(1, total + 1):
    while True:
        try:
            grade = float(input(f"Enter grade {number}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid grade. Please enter a number.")


# Use functions from the imported module
average = get_average(grades)
status = get_status(grades)

highest = student_utils.get_highest(grades)
lowest = student_utils.get_lowest(grades)


# Display report
print("\n===== STUDENT GRADE REPORT =====")
print("Total Grades:", len(grades))
print("Grades:", grades)
print("Average:", round(average, 2))
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Status:", status)

# Display date and time using datetime
current_time = datetime.now()

print("Report Date and Time:", current_time.strftime("%B %d, %Y - %I:%M %p"))
