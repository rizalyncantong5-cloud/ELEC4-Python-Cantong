
# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P5 - Student File Management System
# Date: November 17, 2026

import csv
from pathlib import Path

# File path: Always use students.txt in this program's folder
FILE_NAME = Path(__file__).resolve().parent / "students.txt"


# Function 1: Load student records
def load_records():
    students = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4:
                    student = {
                        "id": row[0],
                        "name": row[1],
                        "program": row[2],
                        "grade": row[3]
                    }
                    students.append(student)

    except FileNotFoundError:
        print("No existing records found. Starting with an empty file.")

        with open(FILE_NAME, "w", newline="") as file:
            pass

    except PermissionError:
        print("Error: You do not have permission to access the file.")

    except OSError as error:
        print("File error:", error)

    return students


# Function 2: Save student records
def save_records(students):
    try:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            for student in students:
                writer.writerow([
                    student["id"],
                    student["name"],
                    student["program"],
                    student["grade"]
                ])

        return True

    except PermissionError:
        print("Error: You do not have permission to save the file.")

    except OSError as error:
        print("Error saving records:", error)

    return False


# Function 3: Add a student
def add_student(students):
    print("\n===== ADD STUDENT =====")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Full Name: ").strip()
    program = input("Enter Program and Section: ").strip()

    if not name or not program:
        print("Name and program cannot be empty.")
        return

    try:
        grade = float(input("Enter Grade: "))

        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid grade. Please enter a number.")
        return

    new_student = {
        "id": student_id,
        "name": name,
        "program": program,
        "grade": str(grade)
    }

    students.append(new_student)

    if save_records(students):
        print("Student record added successfully!")


# Function 4: Display all students
def display_students(students):
    print("\n===== ALL STUDENT RECORDS =====")

    if not students:
        print("No student records available.")
        return

    for student in students:
        print("------------------------------")
        print("Student ID:", student["id"])
        print("Full Name:", student["name"])
        print("Program:", student["program"])
        print("Grade:", student["grade"])


# Function 5: Search student by ID
def search_student(students):
    print("\n===== SEARCH STUDENT =====")

    student_id = input("Enter Student ID to search: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"] == student_id:
            print("\nStudent record found!")
            print("------------------------------")
            print("Student ID:", student["id"])
            print("Full Name:", student["name"])
            print("Program:", student["program"])
            print("Grade:", student["grade"])
            return

    print("Student record not found.")


# Function 6: Update student information
def update_student(students):
    print("\n===== UPDATE STUDENT =====")

    student_id = input("Enter Student ID to update: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"] == student_id:
            print("\nStudent record found!")
            print("Leave the field blank to keep its current value.")

            new_name = input(
                "Enter new name (" + student["name"] + "): "
            ).strip()

            new_program = input(
                "Enter new program (" + student["program"] + "): "
            ).strip()

            new_grade = input(
                "Enter new grade (" + student["grade"] + "): "
            ).strip()

            if new_name:
                student["name"] = new_name

            if new_program:
                student["program"] = new_program

            if new_grade:
                try:
                    grade = float(new_grade)

                    if grade < 0 or grade > 100:
                        print("Grade must be between 0 and 100.")
                        return

                    student["grade"] = str(grade)

                except ValueError:
                    print("Invalid grade. Please enter a number.")
                    return

            if save_records(students):
                print("Student information updated successfully!")

            return

    print("Student record not found.")


# Main program
def main():
    students = load_records()

    while True:
        print("\n===== STUDENT FILE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Information")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_student(students)

            elif choice == "2":
                display_students(students)

            elif choice == "3":
                search_student(students)

            elif choice == "4":
                update_student(students)

            elif choice == "5":
                print("Thank you for using the program!")
                break

            else:
                print("Invalid choice. Please select 1 to 5.")

        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            break

        finally:
            print("Menu operation finished.")


# Run the program
if __name__ == "__main__":
    main()
