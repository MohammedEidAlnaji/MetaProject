class Course:
    def __init__(self, course_name, course_level, course_id=None):
        self.course_name = course_name
        self.course_level = course_level
        self.course_id = course_id

class Student:
    def __init__(self, student_name, student_level, student_id=None):
        self.student_name = student_name
        self.student_level = student_level
        self.student_id = student_id
        self.student_courses = []

    def create_course(self, course_name, course_level):
        # Check if the course level is valid (A, B, C)
        if course_level in ['A', 'B', 'C']:
            course = Course(course_name, course_level, self.course_id_counter)
            self.courses.append(course)
            self.course_id_counter += 1
            print(f"Course '{course.course_name}' created successfully.")
        else:
            print("Invalid course level. Please enter a valid level (A, B, C).")

    def display_details(self):
        print("Student Details:")
        print("Name:", self.student_name)
        print("Class:", self.student_level)
        print("Courses Enrolled:")
        for course in self.student_courses:
            print("-", course.course_name)

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.student_id_counter = 1
        self.course_id_counter = 1

    def add_student(self, student):
        # Check if the student level is valid (A, B, C)
        if student.student_level.upper() in ['A', 'B', 'C']:
            self.students.append(student)
            student.student_id = self.student_id_counter
            self.student_id_counter += 1
            print(f"Student '{student.student_name}' added successfully.")
        else:
            print("Invalid student level. Please enter a valid level (A, B, C).")

    def remove_student(self, student_id):
        # Remove a student based on their ID
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student delete done successfully.")
                return
        print("User does not exist.")

    def edit_student(self, student_id, new_name, new_level):
        # Edit student details based on their ID
        for student in self.students:
            if student.student_id == student_id:
                student.student_name = new_name
                student.student_level = new_level
                print("Student details updated successfully.")
                return
        print("User does not exist.")

    def display_all_students(self):
        # Display details of all students
        print("All Students:")
        for student in self.students:
            print("ID:", student.student_id)
            print("Name:", student.student_name)
            print("Class:", student.student_level)
            print("Courses Enrolled:")
            for course in student.student_courses:
                print("-", course.course_name)
            print()

    def create_course(self, course_name, course_level):
        # Check if the course level is valid (A, B, C)
        if course_level.upper() in ['A', 'B', 'C']:
            course = Course(course_name, course_level, self.course_id_counter)
            self.courses.append(course)
            self.course_id_counter += 1
            print(f"Course '{course.course_name}' created successfully.")
        else:
            print("Invalid course level. Please enter a valid level (A, B, C).")

    def add_course_to_student(self, student_id, course_id):
        # Add a course to a student based on their IDs
        student = None
        for s in self.students:
            if s.student_id == student_id:
                student = s
                break

        if student:
            course = None
            for c in self.courses:
                if c.course_id == course_id:
                    course = c
                    break

            if course:
                student.add_course(course)
            else:
                print("Course does not exist.")
        else:
            print("Student does not exist.")

    def find_student_by_name(self, name):
        # Find and display a student's details by their name
        for student in self.students:
            if student.student_name == name:
                student.display_details()
                return
        print("Student not found.")

    def find_student_by_id(self, student_id):
        # Find and display a student's details by their ID
        for student in self.students:
            if student.student_id == student_id:
                student.display_details()
                return
        print("Student not found.")

# Create an instance of the SchoolSystem class
school_system = SchoolSystem()

while True:
    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display all students")
    print("5. Create new Course")
    print("6. Add Course to Student")
    print("7. Find Student by Name")
    print("8. Find Student by ID")
    print("Q: Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter student name: ")
        student_level = input("Enter student level (A, B, C): ")
        student = Student(student_name, student_level)
        school_system.add_student(student)

    elif choice == "2":
        student_id = int(input("Enter student ID: "))
        school_system.remove_student(student_id)

    elif choice == "3":
        student_id = int(input("Enter student ID: "))
        new_name = input("Enter new name: ")
        new_level = input("Enter new level (A, B, C): ")
        school_system.edit_student(student_id, new_name, new_level)

    elif choice == "4":
        school_system.display_all_students()

    elif choice == "5":
        course_name = input("Enter course name: ")
        course_level = input("Enter course level (A, B, C): ")
        school_system.create_course(course_name, course_level)

    elif choice == "6":
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        school_system.add_course_to_student(student_id, course_id)
    
    elif choice == "7":
        student_name = input("Enter student name: ")
        school_system.find_student_by_name(student_name)

    elif choice == "8":
        student_id = int(input("Enter student ID: "))
        school_system.find_student_by_id(student_id)

    elif choice == "Q":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")
