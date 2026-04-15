command = ""
started = False 
while command != "quit":
    command = input("> ")

    if command == "start":
        if started:      
            print("Car is already started")
        else:
            started = True
            print("Car has Started...")
    elif command == "stop":
        if not started:
            print("Car has already stopped!")
        else:
            started = False
            print("Car has stopped") 
    elif command == "help" :
        print(""" 
start- To start Car
stop- To stop Car 
quit- To Quit
       """)    
    elif command == "quit":
        break       
    else:
        print("I don't understand that")    