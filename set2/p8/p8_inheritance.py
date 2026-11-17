
# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P8 - Inheritance and Polymorphism
# Date: November 17, 2026


# Parent class
class Person:
    def __init__(self, name, age):
        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        self.name = name
        self.age = age

    def introduce(self):
        print("Hello! My name is", self.name)
        print("I am", self.age, "years old.")


# Student inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)

        if not student_id.strip():
            raise ValueError("Student ID cannot be empty.")

        if not course.strip():
            raise ValueError("Course cannot be empty.")

        self.student_id = student_id
        self.course = course

    # Override the introduce method
    def introduce(self):
        print("\n===== STUDENT INFORMATION =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.student_id)
        print("Course:", self.course)
        print("I am currently studying at the university.")


# Teacher inherits from Person
class Teacher(Person):
    def __init__(self, name, age, subject, department):
        super().__init__(name, age)

        if not subject.strip():
            raise ValueError("Subject cannot be empty.")

        if not department.strip():
            raise ValueError("Department cannot be empty.")

        self.subject = subject
        self.department = department

    # Override the introduce method
    def introduce(self):
        print("\n===== TEACHER INFORMATION =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)
        print("Department:", self.department)
        print("I am a teacher who guides students in learning.")


# Create different objects
person1 = Person("Alex Cruz", 30)

student1 = Student(
    "Rizalyn Cantong",
    21,
    "2026-001",
    "BS Information Technology"
)

teacher1 = Teacher(
    "Ma'am Harlyn",
    35,
    "Information Management",
    "Information Technology"
)


# Store different objects in one list.
people = [person1, student1, teacher1]


# Polymorphism: each object uses its own introduce() method.
print("===== PEOPLE INTRODUCTION SYSTEM =====")

for person in people:
    person.introduce()


# Test invalid age validation.
print("\n===== TEST INVALID AGE =====")

try:
    invalid_person = Person("Test Person", 0)
except ValueError as error:
    print("Validation Error:", error)


# Test empty student ID validation.
print("\n===== TEST EMPTY STUDENT ID =====")

try:
    invalid_student = Student(
        "Test Student",
        20,
        " ",
        "BS Information Technology"
    )
except ValueError as error:
    print("Validation Error:", error)


# Test empty course validation.
print("\n===== TEST EMPTY COURSE =====")

try:
    invalid_student = Student(
        "Test Student",
        20,
        "2026-004",
        " "
    )
except ValueError as error:
    print("Validation Error:", error)


# Test empty teacher subject validation.
print("\n===== TEST EMPTY TEACHER SUBJECT =====")

try:
    invalid_teacher = Teacher(
        "Test Teacher",
        35,
        " ",
        "Information Technology"
    )
except ValueError as error:
    print("Validation Error:", error)


# Test empty teacher department validation.
print("\n===== TEST EMPTY TEACHER DEPARTMENT =====")

try:
    invalid_teacher = Teacher(
        "Test Teacher",
        35,
        "Information Management",
        " "
    )
except ValueError as error:
    print("Validation Error:", error)


# Explanation:
# Inheritance allows a child class to reuse the attributes and methods of a parent class.
# The Student and Teacher classes inherit the name and age attributes from Person.
# The super() function calls the constructor of the parent class.
# Polymorphism allows different objects to use the same method name but perform different actions.
# In this program, each object has its own version of the introduce() method.
