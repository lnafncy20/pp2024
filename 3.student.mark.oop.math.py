import math
import numpy as np

# Student class
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    # Add mark method
    def add_mark(self, course, mark):
        # Use math.floor() to round down the mark to 1 decimal place
        self.marks[course] = math.floor(float(mark) * 10) / 10

    # Calculate GPA method
    def calculate_gpa(self, courses):
        total_credit = 0
        weighted_sum = 0
        for course, mark in self.marks.items():
            credit = next((c.credit for c in courses if c.name == course), None)
            if credit:
                total_credit += float(credit)
                weighted_sum += float(mark) * float(credit)
        if total_credit == 0:
            return 0
        else:
            return round(weighted_sum / total_credit, 1)

# Course class
class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

# School class
class School:
    def __init__(self):
        self.students = []
        self.courses = []

    # Input students method
    def input_students(self):
        total_student = int(input("Enter the number of students: "))
        for _ in range(total_student):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            self.students.append(Student(id, name, dob))

    # Input courses method
    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = input("Enter course credit: ")
            self.courses.append(Course(id, name, credit))

    # Input marks method
    def input_marks(self):
        course_id = input("Enter the course ID to input marks for: ")
        for course in self.courses:
            if course.id == course_id:
                for student in self.students:
                    mark = input(f"Enter mark for student {student.name}: ")
                    student.add_mark(course.name, mark)

    # Show students method
    def show_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}")

    # Show student marks method
    def show_student_marks(self):
        for student in self.students:
            print(f"Student: {student.name}")
            for course, mark in student.marks.items():
                print(f"Course: {course}, Mark: {mark}")

    # Show courses method
    def show_courses(self):
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}, Credit: {course.credit}")

    # Show GPA method
    def show_gpa(self):
        for student in self.students:
            gpa = student.calculate_gpa(self.courses)
            print(f"Student: {student.name}, GPA: {gpa}")

    # Sort students by GPA descending
    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.calculate_gpa(self.courses), reverse=True)

# Main function
def main() :
    school = School()
    school.input_students()
    school.input_courses()
    
    while True:
        print('''
        Welcome to the Student Management System:
            0. Exit
            1. Select a course and input marks for students in this course
            2. Show list of students
            3. Show list of courses
            4. Show student marks
            5. Show GPAs of all students
            6. Sort students by GPA descending
            ''')
        
        option = int(input("Enter your choice: "))

        if option == 0:
            break
        elif option == 1:
            school.input_marks()
        elif option == 2:
            school.show_students()
        elif option == 3:
            school.show_courses()
        elif option == 4:
            school.show_student_marks()
        elif option == 5:
            school.show_gpa()
        elif option == 6:
            school.sort_students_by_gpa()
            print("Students sorted by GPA:")
            school.show_students()
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

# Call the main function
if __name__ == "__main__":
    main()