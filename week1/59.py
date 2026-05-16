''' Default Arguments
Write a function introduce(name, age, city='Unknown') that returns 'I am [name],
 [age] years old, from [city].' Call it:

With all three arguments
With only name and age (city should default)
With city passed as a keyword argument
'''
def introduce(name,age,city = 'unknown'):
    return "I am " + name + ", " + str(age) + " years old , from " + city + "."


result = introduce("Jeet",22,"Valsad")
print(result)


result_1 = introduce("Krishi",20)
print(result_1)

result_2 = introduce("Frenny",13,city = "Mumbai")
print(result_2)