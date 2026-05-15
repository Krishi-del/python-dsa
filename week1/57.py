#word reverser function
def reverse_words(sentence):
    words =  sentence.split(" ")
    words = words[::-1]
    print(" ".join(words))
    return words
reverse_words("Python - a programming language")

