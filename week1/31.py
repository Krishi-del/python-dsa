number = 9
tries = 0
while True:
    guess = int(input("Guess the number: "))
    tries+=1
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    elif guess == number:
        print("Correct!")
        break
print("number of tries: ",tries)
    