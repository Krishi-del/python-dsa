#fizzbuzz
n = int(input("Enter digit:"))

if n % 3 == 0 :
    if n% 5 ==0:
        print("Fizzbuzz")
    else:
        print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print("None")                