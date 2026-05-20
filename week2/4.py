'''
Squares
Using a list comprehension, 
generate a list of squares for numbers 1 through 10. 
Then do the same but only for even numbers.
'''
num1 = [i**2 for i in range(1,11)]
num = [i**2 for i in range(1,11) if i % 2 == 0]
print(num1)
print(num)

'''
String Lengths
Given words = ['python', 'is', 'awesome', 'and', 'fun'], use a list comprehension
to create a list of the lengths of each word. 
Then create another that keeps only words longer than 3 characters.
'''
words = ['python', 'is', 'awesome', 'and', 'fun']
le = [len(word) for word in words]
j = [n for n in words if len(n) > 3]
print(j)
print(le)