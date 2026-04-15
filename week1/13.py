# while loop
# guess game
secret_number = 9
guess_try = 3
guess_count = 0
while guess_try > guess_count:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You Failed!")    
