def emoji_converter(message):
    words = message.split(' ')
    emoji = {
        ":)":"😊",
        ":(" : "😔"
    }
    output = ""
    for ch in words:
        output += emoji.get(ch, ch) + ""
    return output


message = input("> ")
print(emoji_converter(message)) 
