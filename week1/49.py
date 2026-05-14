'''List Builder with Loop
Ask the user to enter 5 numbers one by one. Append each to an empty list. 
Then print the list, its sum, and whether the list is sorted in ascending 
order (check using a loop — don't use sorted()).
'''
num = []
for i in range(5):
    n = int(input("Enter a number: "))
    num.append(n)

print(num) 
total = 0
for n in num:
    total+=n
print("Sum: ", total)

highest = num[0]
for i in num:
    if i>highest:
        i = highest
        


