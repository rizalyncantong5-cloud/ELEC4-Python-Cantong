
# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P4 - Exception Handling
# Date: November 17, 2026

# Function 1: Divide two numbers safely
def divide_numbers():
    print("\n===== DIVISION =====")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        answer = first_number / second_number

    except ValueError:
        print("Invalid input. Please enter numbers only.")

    except ZeroDivisionError:
        print("Cannot divide a number by zero.")

    else:
        print("Result:", answer)

    finally:
        print("Division operation finished.")


# Function 2: Read a text file
def read_file():
    print("\n===== FILE READER =====")

    file_name = input("Enter the file name: ").strip()

    if not file_name:
        print("File name cannot be empty.")
        print("File reading operation finished.")
        return

    try:
        with open(file_name, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: The requested file does not exist.")

    except PermissionError:
        print("Error: You do not have permission to open this file.")

    else:
        print("\n===== FILE CONTENTS =====")
        if content:
            print(content)
        else:
            print("The file is empty.")

    finally:
        print("File reading operation finished.")


# Main menu
while True:
    print("\n===== EXCEPTION HANDLING PROGRAM =====")
    print("1. Divide Two Numbers")
    print("2. Open a Text File")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            divide_numbers()

        elif choice == 2:
            read_file()

        elif choice == 3:
            print("Thank you for using the program!")
            break

        else:
            print("Invalid menu choice. Please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter a menu number.")

    finally:
        print("Menu operation finished.")
