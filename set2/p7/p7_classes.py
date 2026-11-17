
# Name: Rizalyn A. Cantong
# Section: IV-BSIT A
# Activity: P7 - Classes and Objects
# Date: November 17, 2026


class Subject:
    def __init__(self, subject_name, teacher):
        self.subject_name = subject_name
        self.teacher = teacher

    def display_subject(self):
        print("Subject:", self.subject_name)
        print("Teacher:", self.teacher)


class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.__grade = 0
        self.set_grade(grade)

    # Getter: returns the student's private grade.
    def get_grade(self):
        return self.__grade

    # Setter: accepts only grades from 0 to 100.
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            return True
        else:
            print("Invalid grade! Grade must be from 0 to 100.")
            return False

    def update_grade(self, new_grade):
        if self.set_grade(new_grade):
            print("Grade updated successfully!")
            return True
        return False

    def display_student(self):
        print("------------------------------")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Grade:", self.get_grade())


class Section:
    def __init__(self, section_name, subject):
        self.section_name = section_name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        # Check if the student ID already exists.
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("Student ID already exists!")
                return False

        self.students.append(student)
        return True

    # Search for a student using their ID.
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def display_section(self):
        print("\n===== SECTION:", self.section_name, "=====")
        self.subject.display_subject()

        print("\n===== STUDENT LIST =====")
        for student in self.students:
            student.display_student()

        print("------------------------------")
        print("Total Students:", len(self.students))


# Create a subject object.
subject_info = Subject("Information Management", "Ma'am Harlyn")

# Create three student objects.
student1 = Student("2026-001", "Rizalyn Cantong", 95)
student2 = Student("2026-002", "Kingsley Hilario", 90)
student3 = Student("2026-003", "Jai Santos", 88)

# Create a section and add the students.
bsit_section = Section("BSIT 4A", subject_info)

bsit_section.add_student(student1)
bsit_section.add_student(student2)
bsit_section.add_student(student3)

# Display the original student information.
print("===== ORIGINAL STUDENT RECORDS =====")
bsit_section.display_section()

# Test duplicate student ID validation.
print("\n===== TEST DUPLICATE STUDENT ID =====")
duplicate_student = Student("2026-001", "Test Student", 85)
bsit_section.add_student(duplicate_student)

# Search for a student using their ID.
print("\n===== SEARCH STUDENT BY ID =====")
search_id = input("Enter Student ID to search: ")

found_student = bsit_section.find_student(search_id)

if found_student:
    print("Student found!")
    found_student.display_student()
else:
    print("Student ID not found!")

# Update the grade of one student.
print("\n===== UPDATE STUDENT GRADE =====")
print("Student:", student2.name)
student2.update_grade(98)

# Display the updated student information.
print("\n===== UPDATED STUDENT RECORDS =====")
bsit_section.display_section()
