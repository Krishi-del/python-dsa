'''
Squares
Using a list comprehension, 
generate a list of squares for numbers 1 through 10. 
Then do the same but only for even numbers.
'''
n = [m**2 for m in range(1,11)]
sq = [num**2 for num in range(1,11) if num % 2 == 0]

print(n)
print(sq)
'''
String Lengths
Given words = ['python', 'is', 'awesome', 'and', 'fun'], use a list comprehension
to create a list of the lengths of each word. 
Then create another that keeps only words longer than 3 characters.
'''
words = ['python', 'is', 'awesome', 'and', 'fun']
length = [len(word) for word in words]
print(length)
ch = [word for word in words if len(word) > 3]
print(ch)