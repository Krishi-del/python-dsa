sentence = 'hello, welcome to PYTHON programming! '
print(sentence.strip())
print(sentence.title())
print(sentence.replace('PYTHON','Python'))
print(sentence.find('welcome'))
print(sentence.split())
print(len(sentence))

#tuple coordinates
point = (4,7)
#point[0] = 8 tuples are immutable
x,y = point
print(x,y)

point1 = [4,7]
point1[0] = 8
a,b = point1
print(a,b)