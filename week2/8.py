'''
Multiplication Table as Nested List
Use a nested list comprehension to build a 5x5 multiplication table as a list of lists.
Then print it in grid format using a nested for loop.
'''

table = [[i*j for j in range(1,6)] for i in range(1,6)]
print(table)
for row in table:
    for value in row:
        print(value,end = "\t")
    print()    

#shallow vs deep copy

import copy
a = [[1,2], [3,4]]
b = copy.copy(a)
b[0][1] = 5  # shallow copy- after value is changed, both a and b changes
print(a,b) 

c = [[6,7],[8,9]]
d = copy.deepcopy(c)
d  [0][1] = 10 #deep copy does not change original value
print(c,d) 

#lambda function
sq = lambda x : x*x 
print(sq(5))

#imediate invoke
print((lambda x,y: x+y) (4,5))

#enumerate
fruits = ['Mango','Orange','Apple']
for index, i in enumerate(fruits):
    print(index , "->", i)

#zip()
names = ['A','B']
l_name = ['C','D']
print(list(zip(names,l_name)))  #have to convert to list

#sorting
course = ['Maths','History','CSE','Art']
l = sorted(course) # sorted() function creates a new variable and stores the sorted list 
print(l)

courses = ['B','U','H']
courses.sort()
print(courses) #.sort() method sorts original list 