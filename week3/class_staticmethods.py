class Employee:

    raise_amt = 1.04

    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    #class method
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
date = datetime.date(2025,5,5)
print(Employee.is_workday(date))

emp_str_1 = 'John-Doe-20000'
emp_str_2 = 'Suhani-Patel-30000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

emp1 = Employee('Rahul', 25,20000)
emp2 = Employee('Priya', 24,30000)

Employee.set_raise_amt(1.06)

print(emp1.raise_amt)
print(emp2.raise_amt)

print(new_emp_1.name)
print(new_emp_2.pay)