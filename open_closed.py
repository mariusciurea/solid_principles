"""O - Open Closed

Author: Bertrand Meyer
Principle: Functions, classes, modules should be open for extension, but closed for modification
"""

# ==================================================================================
# This violates the Open Closed principle
# ==================================================================================

class Employee:
    def __init__(self, firstname, lastname, pid, department):
        self.firstname = firstname
        self.lastname = lastname
        self.pid = pid
        self.department = department
        if self.department == 'HR':
            self.salary_range = (1000, 2000)
        elif self.department == 'Finance':
            self.salary_range = (700, 1800)
        elif self.department == 'IT':
            self.salary_range = (1200, 2000)

    def average_income(self):
        if self.department == 'HR':
            return (self.salary_range[0] + self.salary_range[1]) / 2
        elif self.department == 'Finance':
            return (self.salary_range[0] + self.salary_range[1]) / 2
        if self.department == 'IT':
            return (self.salary_range[0] + self.salary_range[1]) / 2


emp = Employee('Diana', 'Popescu', 12333, 'IT')
print(emp.average_income())


# =================================================================================
#               This follows the Open Closed principle
# =================================================================================

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, department):
        self.department = department

    @abstractmethod
    def average_income(self):
        pass


class HREmployee(Employee):
    def __init__(self, firstname, lastname, pid):
        super().__init__('HR')
        self.firstname = firstname
        self.lastname = lastname
        self.pid = pid
        self.salary_range = (1000, 2000)

    def average_income(self):
        return (self.salary_range[0] + self.salary_range[1]) / 2


class ITEmployee(Employee):
    def __init__(self, firstname, lastname, pid, annual_bonus):
        super().__init__('IT')
        self.firstname = firstname
        self.lastname = lastname
        self.pid = pid
        self.salary_range = (1300, 2300)
        self.annual_bonus = annual_bonus

    def average_income(self):
        return (self.salary_range[0] + self.salary_range[1]) / 2 + self.annual_bonus


hr_emp = HREmployee('Marius', 'Ciurea', 11223333)
it_emp = ITEmployee('Marian', 'Dudea', 11223334, 300)
print(hr_emp.average_income())
print(it_emp.average_income())
