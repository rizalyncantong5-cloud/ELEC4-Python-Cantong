
# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P2 - Student Utility Functions
# Date: November 17, 2026

# Function 1: Calculate the average grade
def get_average(grades):
    return sum(grades) / len(grades)


# Function 2: Determine the student's status
def get_status(grades):
    average = get_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 3: Get the highest grade
def get_highest(grades):
    return max(grades)


# Function 4: Get the lowest grade
def get_lowest(grades):
    return min(grades)
