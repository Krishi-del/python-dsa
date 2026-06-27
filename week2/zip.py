#zip()
num  = [1,2,3]
letters = ['a','b','c']

zipped = zip(num,letters)
print(zipped)  #prints iterable object. To consume it use list()

print(list(zipped))

#zip() when arguments of unequal length

a = range(5)
print(list(zip(letters,a)))

#one argument

b = range(3)
print(list(zip(b)))

#zip_longest
l = range(12)
from itertools import zip_longest
print(list(zip_longest(l,letters, fillvalue= '?')))

#keyword argument strict
#by default strict = False 
a = range(5)
print(list(zip(letters,a , strict = True))) 
#raises a ValueError

#iterating 

for n, letter in zip(num,letters):
    print(f'Number : {n}')
    print(f'Letter : {letter}')

#parallel iteration 
