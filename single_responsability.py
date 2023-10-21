# ############### S - Single Responsibility ########################
# Author: Uncle Bob (Robert C. Martin) - Agile Manifesto signatories
# Principle: A class should have only one reason to change - A class should have only 1 responsibility


# This violates the Single Responsibility principle

# class Student:
#     def __init__(self, firstname, lastname, university, cnp):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.university = university
#         self.cnp = cnp
#
#     @property
#     def email(self):
#         return f'{self.firstname.lower()}.{self.lastname.lower()}@{self.university.lower()}.com'
#
#     def save_student_info(self):
#         info = f'{self.firstname}\n' \
#                f'{self.lastname}\n' \
#                f'{self.university}\n' \
#                f'{self.email}\n'
#         with open('student.txt', 'w') as f:
#             f.write(info)


# This follows the Single Responsibility principle

class Student:
    def __init__(self, firstname, lastname, university, cnp):
        self.firstname = firstname
        self.lastname = lastname
        self.university = university
        self.cnp = cnp

    @property
    def email(self):
        return f'{self.firstname.lower()}.{self.lastname.lower()}@{self.university.lower()}.com'


class SaveStudentToText:
    def __init__(self, student_path):
        self.path = student_path

    def save_student(self, student: Student):
        student_data = f'{student.firstname}, {student.lastname} - {student.cnp}'
        with open(self.path, 'w') as fw:
            fw.write(student_data)

