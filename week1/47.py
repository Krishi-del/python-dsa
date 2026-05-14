'''List Membership
Ask the user to enter a name. Check if that name is in 
guests = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']. Print 'Welcome!' or 'Not on the list.'.
Then print the list sorted alphabetically without modifying the original.
'''
guests = ['Bob', 'Alice', 'Diana', 'Charlie', 'Eve']

name = input("Enter your name: ")
if name in guests:
    print("Welcome!")
else:
    print("Not on the list.") 


    print(sorted(guests))
print(guests)        