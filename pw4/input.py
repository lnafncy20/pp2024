from domains.student import Student
from domains.course import Course

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