class Dog:

    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age =  age

    def description(self):
        return f'{self.name} is {self.age} years old' #output will be something like <__main__.Dog object at 0x00000179D33F6A50>
    
    def __str__(self):
        return f'{self.name} is {self.age} years old'
dog1 = Dog('Marcel', 4)
dog2 = Dog('Shero',8)

print(dog1) 


print(dog1.name)

print(dog2.species)

dog2.species = 'Golden retriever'

print(dog2.species)

print(dog2.description())