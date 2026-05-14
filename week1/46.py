'''
Sum and Average
Given marks = [78, 92, 85, 67, 90, 55, 88], use a for loop (no sum()) to calculate
the total and average. Print both rounded to 2 decimal places.
'''
marks = [78, 92, 85, 67, 90, 55, 88]
total=0

for i in marks:
    total+=i
average = total/len(marks)   
print("Total", round(total,2))
print("Average",round(average,2))