import input as input_module  # Rename input module to avoid conflicts with built-in input function
import output
from domains.student import Student
from domains.course import Course
from domains.school import School

def main():
    school = School()
    if not input_module.check_and_decompress():  # Use input_module alias to access functions from input.py
        students_data = input_module.input_students()
        for student_data in students_data:
            school.students.append(Student(student_data['id'], student_data['name'], student_data['dob']))

        courses_data = input_module.input_courses()
        for course_data in courses_data:
            school.courses.append(Course(course_data['id'], course_data['name'], course_data['credit']))

        marks_data = input_module.input_marks(school.students, school.courses)
        for mark_data in marks_data:
            for student in school.students:
                if student.name == mark_data['student']:
                    student.add_mark(mark_data['course'], mark_data['mark'])
        
        input_module.compress_files()

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
            marks_data = input_module.input_marks(school.students, school.courses)
            for mark_data in marks_data:
                for student in school.students:
                    if student.name == mark_data['student']:
                        student.add_mark(mark_data['course'], mark_data['mark'])
        elif option == 2:
            output.show_students([(s.id, s.name, s.dob) for s in school.students])
        elif option == 3:
            output.show_courses([(c.id, c.name, c.credit) for c in school.courses])
        elif option == 4:
            output.show_student_marks([(m['course'], m['student'], student.marks[m['course']]) for student in school.students for m in student.marks.items()])
        elif option == 5:
            output.show_gpa([(s.name, s.calculate_gpa(school.courses)) for s in school.students])
        elif option == 6:
            school.sort_students_by_gpa()
            print("Students sorted by GPA:")
            output.show_students([(s.id, s.name, s.dob) for s in school.students])
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
