'''
A cinema charges tickets based on age and day: adults (18+) pay ₹200 on weekdays, 
₹300 on weekends. Children (under 18) pay ₹100 any day. Seniors (60+) are free. 
Write the pricing logic.
'''
age = int(input("Enter age: "))
day = input("Enter day: ").lower
if age>=60:
    print("Free!")
elif age<18:
    print("100")    
else:
    if day == "Saturday" or day == "Sunday":
        print("200")
    else:
        print("300")
            