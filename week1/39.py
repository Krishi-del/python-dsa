'''
Number Pyramid 
Print this pattern for 5 rows using nested loops:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
rows = 5
for i in range(1, rows+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()    
