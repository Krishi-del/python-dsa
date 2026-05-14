n = (input("Phone: "))
digits = {
    "1" : "one",
    "2" : "two",
    "3": "three",
    "4" : "four"
}
output = ""
for ch in n:
    output += digits.get(ch,"!") + " "
print(output)
