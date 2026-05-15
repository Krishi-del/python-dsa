#checkpoint- CLI calculator
history = []
while True:
    print("CLI Calculator")
    choice = input("Select from below \n 1.Calculate \n 2.View History \n 3.Exit\n")
    if choice == "1":
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator(+,-,*,/):  ")
        num2 = float(input("Enter second number: "))
        try:
            if operator == "+":
                result =  num1+num2
            elif operator == "-":
                result =  num1-num2
            elif operator == "*":
                result =  num1*num2 
            elif operator == "/":
                result = num1/num2 
            else:
                print("Invalid operator")
                continue
            print(f"{num1} {operator} {num2} = {result}")
            history.append(f"{num1} {operator} {num2} = {result}") 
        except ZeroDivisionError:
            print("Cannot divide by zero")
    elif choice == "2":
        print("History") 
        if len(history) == 0:
            print("No history found")
        else:   
            print(history)
    elif choice == "3":
        print("Byee") 
        break