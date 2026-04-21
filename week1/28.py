#day 3 concepts
"""Print the multiplication table of any number from 1 to 10 using a for loop and range(). 
Format it neatly: "7 x 3 = 21"
"""
num = int(input("Enter number "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")