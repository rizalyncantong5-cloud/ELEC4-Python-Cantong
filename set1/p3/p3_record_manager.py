# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P3 - Student Record Manager
# Date: November 17, 2026

# List for storing student names
student_list = []

# Set for checking duplicate names
name_checker = set()


# Function 1: Add a student
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    if name.casefold() in name_checker:
        print("Student already exists!")
    else:
        student_list.append(name)
        name_checker.add(name.casefold())
        print("Student added successfully!")


# Function 2: Remove a student
def remove_student():
    name = input("Enter the name to remove: ").strip()

    if name.casefold() in name_checker:
        for student in student_list:
            if student.casefold() == name.casefold():

                confirm = input(
                    f"Are you sure you want to remove {student}? (yes/no): "
                ).strip().casefold()

                if confirm == "yes":
                    student_list.remove(student)
                    name_checker.remove(student.casefold())
                    print("Student removed successfully!")
                else:
                    print("Student removal cancelled.")

                return
    else:
        print("Student not found.")


# Function 3: Search for a student
def search_student():
    keyword = input("Enter name to search: ").strip().casefold()

    if keyword == "":
        print("Please enter a name to search.")
        return

    matches = [
        student for student in student_list
        if keyword in student.casefold()
    ]

    if matches:
        print("\n===== SEARCH RESULTS =====")
        for student in matches:
            print(student)
    else:
        print("No matching student found.")


# Function 4: Display all students
def display_students():
    print("\n===== STUDENT RECORDS =====")

    if not student_list:
        print("No student records available.")
        return

    sorted_names = sorted(student_list, key=str.casefold)

    for number, student in enumerate(sorted_names, start=1):
        print(f"{number}. {student}")

    print("Total Students:", len(student_list))


# Main menu
while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank you for using the Student Record Manager!")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")


# LIST AND SET:
# A list stores student names and allows the program to display them in order.
# A set stores unique name keys and helps prevent duplicate student records.
# Lists can contain duplicate values, while sets only keep unique values.
# In this program, the list manages the records while the set checks duplicates.
