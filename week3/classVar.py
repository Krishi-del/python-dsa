class Employee:
    raise_amt = 1.04
    num_of_emps = 0   #class variable

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
print(Employee.num_of_emps)

em1 = Employee('Jeet','Tandel', 50000)    

print(Employee.num_of_emps)

em2 = Employee('Krishi' ,'Tandel',50000)

print(Employee.num_of_emps)

print(em1.first)

print(Employee.fullname(em2))
