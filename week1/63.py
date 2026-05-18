'''Default Greeting
Write a function greet(name, language='English') with a docstring. 
Return greetings in: English ('Hello'), Spanish ('Hola'), French ('Bonjour'), Hindi ('Namaste'). 
Return 'Language not supported' for anything else. Call it 5 times mixing default and custom language.
'''
def greet(name, language = 'English'):
    """ Greetings in different languages """
    if language == "English":
        return name + "Hello"
    elif language == "Spanish":
        return name + "Hola"
    elif language == "French":
        return name + "Bonjor"
    elif language == "Hindi":
        return name + "Namaste"
    else:
        return "Language not supported"
    
greetings = greet("Jeet ", language = "Hindi")
greetings1 = greet("Frenny ")
greetings2 = greet("Dhyani ",language = "Spanish")
greetings3 = greet("Yudhav ",)
greetings4 = greet("Dhairya ", language = "French")
print(greet.__doc__)
print(greetings)
print(greetings1) 
print(greetings2) 
print(greetings3)
print(greetings4)  