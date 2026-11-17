
# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P6 - Recursive Functions
# Date: November 17, 2026

def factorial(n):
    # Base case: factorial of 0 or 1 is 1.
    if n <= 1:
        return 1

    # Recursive call: multiply n by the factorial of n - 1.
    return n * factorial(n - 1)


def fibonacci(n):
    # Base case: the first two Fibonacci values are 0 and 1.
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive call: add the two previous Fibonacci values.
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_numbers(n):
    # Base case: the sum from 1 to 0 is 0.
    if n == 0:
        return 0

    # Recursive call: add n to the sum of the previous numbers.
    return n + sum_numbers(n - 1)


def search(items, target):
    # Base case: an empty list means the target was not found.
    if len(items) == 0:
        return False

    # Base case: the first item matches the target.
    if items[0] == target:
        return True

    # Recursive call: search the remaining items.
    return search(items[1:], target)


def show_menu():
    print("\n===== RECURSION PROGRAM =====")
    print("1. Factorial")
    print("2. Fibonacci Sequence")
    print("3. Sum of Numbers")
    print("4. Search in a List")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            number = int(input("Enter a non-negative number: "))

            if number < 0:
                print("Please enter a non-negative number.")
            else:
                print("Factorial:", factorial(number))

        elif choice == "2":
            number = int(input("How many Fibonacci terms? "))

            if number < 1:
                print("Please enter a number greater than 0.")
            elif number > 30:
                print("Please enter up to 30 terms only.")
            else:
                print("\nFibonacci Sequence:")
                for i in range(number):
                    print(fibonacci(i), end=" ")
                print()

        elif choice == "3":
            number = int(input("Enter a positive number: "))

            if number < 0:
                print("Please enter a non-negative number.")
            else:
                print("Sum:", sum_numbers(number))

        elif choice == "4":
            raw_items = input("Enter numbers separated by commas: ").strip()

            if not raw_items:
                print("Please enter at least one number.")
                continue

            items = [
                int(value.strip())
                for value in raw_items.split(",")
                if value.strip()
            ]

            if not items:
                print("Please enter valid numbers.")
                continue

            target = int(input("Enter number to search: "))

            if search(items, target):
                print(target, "was found in the list.")
            else:
                print(target, "was not found in the list.")

        elif choice == "5":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
