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
