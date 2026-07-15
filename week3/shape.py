#build Shape → Circle, Rectangle, Triangle hierarchy. Each has area() and perimeter() methods
import math
class Shape:

    def __init__(self,name,color):
        self.name = name
        self.color = color

    def area(self):
        raise NotImplementedError('Subclasses must implement area()')
    
    def perimeter(self):
        raise NotImplementedError('Subclasses must implement perimeter()')

class Circle(Shape):

    def __init__(self,name,color,radius):
        super().__init__(name,color)
        self.radius = radius
    
    def area(self):
        return f'Area : {math.pi * self.radius ** 2}'
    
    def perimeter(self):
        return f'Perimeter : {2 * math.pi * self.radius}'
    
class Rectangle(Shape):

    def __init__(self,name,color,length,breadth):
        super().__init__(name,color)
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return f'Area : {self.length * self.breadth}'
    
    def perimeter(self):
        return f'Perimeter : {2 * (self.length + self.breadth)}'
    

class Triangle(Shape):

    def __init__(self,name,color,base,height):
        super().__init__(name,color)
        self.base = base
        self.height = height
    
    def area(self):
        return f'Area : {0.5 * self.base * self.height}'
    

c1 = Circle('Circle1', 'blue', 2)

r1 = Rectangle('Rectangle', 'pink', 20,30)

t1 = Triangle('Triangle', 'red', 2,9)
print(c1.area())
print(c1.perimeter())

print(r1.area())
print(r1.perimeter())

print(t1.area())

