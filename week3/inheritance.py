class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.full_name())

dev1 = Developer('Krishi','Tandel',50000,'Python')   #inherited from Employee class
dev2 = Developer('Rahul', 'Patil', 40000,'Java')
# print(help(Developer))
# print(dev1.email)

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)

# print(dev1.prog_lang)
print(dev1.full_name())
mgr1 = Manager('Jeet','Tandel',90000, [dev1])

# print(mgr1.email)

# mgr1.add_emp(dev2)

# mgr1.print_emps()

# mgr1.remove_emp(dev1)

# mgr1.print_emps()

# print(isinstance(mgr1, Manager))

# print(issubclass(Manager,Employee))