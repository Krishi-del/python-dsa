#lambda
add = lambda x,y : x+y
res = add(1,9)
print(res) 
#positional argument
print((lambda x,y,z : x+y+z) (1,2,3))

#keyword arguments
print((lambda x,y,z=2: x+y+z) (1,2))

print((lambda x,y,z=1 : x+y+z) (1,y=2))

print((lambda *args : sum(args)) (1,2,3,4,5))

print((lambda **kwargs : sum(kwargs.values())) (one = 1, two = 2))

#map() and filter()
print(list(map(lambda x: x.capitalize(), ['cat', 'dog'])))

print(list(filter(lambda x: len(x) > 4, ['cat', 'dog','elephant'])))