#Student class
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
    # Add mark function
    def add_mark(self, course, mark):
        self.marks[course] = mark 

# Course class
class Course:
    def __init__(course, id, name):
        course.id = id
        course.name = name

# School class
class School:
    def __init__(school):
        school.students = []
        school.courses = []

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
            self.courses.append(Course(id, name))

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
            print(f"ID: {course.id}, Name: {course.name}")

# Main function       
def main() :
    school = School()
    school.input_students()
    school.input_courses()
    
    while True:
        print('''
        Welcome to the Student Manangement System:
            0. Exit
            1. Select a course and input marks for student in this course
            2. Show list of students
            3. Show list of courses
            4. Show student marks
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
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Call the functions
if __name__ == "__main__":
    main()