class Car:
    
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f'{self.color} has {self.mileage} miles'    
    
    def __str__(self):
        return f'{self.color} has {self.mileage} '
    
car1 = Car('Blue', 20000)
car2 = Car('Green' , 30000)

print(car1)
print(car2)

#inheritance

# class Dog:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
    
#     def speak(self,sound):
#         return f'{self.name} says {self.sound}'
    
# # ...

# class JackRussellTerrier(Dog):
#     pass

# class Dachshund(Dog):
#     pass

# class Bulldog(Dog):
#     pass

# miles = JackRussellTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)

# print(jack)
# print(miles)

# print(buddy.age)
