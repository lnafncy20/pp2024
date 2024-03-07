import math

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
