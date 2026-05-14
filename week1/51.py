message = input("> ")
words = message.split(' ')
emoji = {
    ":)":"😊",
    ":(" : "😔"
}
output = ""
for ch in words:
    output += emoji.get(ch, ch) + ""
print(output)    