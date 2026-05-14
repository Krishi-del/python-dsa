'''Min and Max Without Built-ins
Given temps = [34, 28, 41, 19, 36, 22, 45, 30], 
find the highest and lowest temperature using a for loop — without using min() or max(). 
Print both with an f-string.
'''
temps = [34, 28, 41, 19, 36, 22, 45, 30]
highest = temps[0]
lowest = temps[0]
for i in temps:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
print(f"Highest temperature is {highest}")
print(f"Lowest temperature is {lowest}")             