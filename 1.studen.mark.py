#Function to input students
def input_students():
    total_student = int(input("Enter the number of students: "))
    students = []

    for i in range(total_student):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")

        student_info = {'id': student_id, 'name': name, 'dob': dob}
        students.append(student_info)

    return students

#Function to input courses
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []

    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")

        course_info = {'id': course_id, 'name': course_name}
        courses.append(course_info)

    return courses

#Function to input marks
def input_marks(students, courses):
    course_id = input("Enter the course ID to input marks for: ")

    for course in courses:
        if course['id'] == course_id:
            for student in students:
                marks = float(input(f"Enter marks for {student['name']} in {course['name']}: "))
                student.setdefault('marks', {})[course_id] = marks

#Function to show list of courses
def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

#Function to show list of students
def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

#Function to show student marks
def show_student_marks(students, courses):
    student_id = input("Enter the student ID to show marks for: ")
    for student in students:
        if student['id'] == student_id:
            print(f"Student: {student['name']}, ID: {student['id']}")
            for course in courses:
                marks = student.get('marks', {}).get(course['id'])
                print(f"  Course: {course['name']}, Marks: {marks if marks is not None else 'N/A'}")

# Main program
def main() :
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
            input_marks(students, courses)
        elif option == 2:
            list_students(students)
        elif option == 3:
            list_courses(courses)
        elif option == 4:
            show_student_marks(students, courses)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Call the functions
if __name__ == "__main__":
    students = input_students()
    courses = input_courses()
    main()