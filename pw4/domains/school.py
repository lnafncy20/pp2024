class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.calculate_gpa(self.courses), reverse=True)
