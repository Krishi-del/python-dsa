#populating manually
student = {} 
student['name'] = 'Jeet'
student['age'] = 21

print(student)

#populating dictionaries using a loop
square = {}
for integer in range(1,11):
    square[integer] = integer**2
print(square)    

#dictionaries comprehension
sq = {integer: integer**2 for integer in range(1,11) }
print(sq)