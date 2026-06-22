'''
Uppercase Filter
Given names = ['alice', 'bob', 'charlie', 'diana', 'eve'], use a list comprehension to:
Uppercase every name
Keep only names with more than 3 letters, uppercased
Create a list of tuples (name, len(name)) for all names
'''
names = ['alice', 'bob', 'charlie', 'diana', 'eve']
u = [name.title() for name in names]
print(u)
j = [name for name in u if len(name) > 3 ]
print(j)
t = [(name, len(name)) for name in u]
print(t)