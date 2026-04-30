''' 
Vending Machine
Set item_price = 35. 
Ask the user how much money they insert. If it's exact, print 'Thank you!'.
If more, print 'Change: ₹[amount]'. If less, print 'Insufficient. Need ₹[amount] more.'
'''
item_price = 35
user_amt = int(input("How much amount did you insert? "))
if user_amt == item_price:
    print("Thank you!")
    
elif user_amt> item_price:
    change = user_amt - item_price
    print("Change: ₹",change)

elif user_amt< item_price:
    need = item_price - user_amt
    print("Insufficient. Need ₹", need)

