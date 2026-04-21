#day 3 concepts 
#Use a while loop to keep asking the user for a number until they enter a negative number. 
# Then print how many valid numbers they entered
tries = 0

while True:
    a = int(input("Enter a number: "))

    if a<0:
        break
    tries+=1
print(tries)    