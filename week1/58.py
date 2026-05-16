'''Calculator Functions
Write four separate functions: add(a, b), subtract(a, b), multiply(a, b), divide(a, b). 
Each should return the result. For divide, return 'Cannot divide by zero' if b is 0. 
Call all four and print results
'''
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
        try:
            return a/b
        except(ZeroDivisionError):
            print("Cannot divide by zero")

add(23,55)
subtract(66,60)
multiply(23,9)
divide(5,0)