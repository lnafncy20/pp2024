from input import input_students, input_courses, input_marks
from output import show_students, show_student_marks, show_courses, show_gpa
from domains.student import Student
from domains.course import Course
from domains.school import School

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