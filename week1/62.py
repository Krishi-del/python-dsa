'''List Report
Given temps = [22.5, 31.0, 18.3, 27.8, 35.1, 20.0, 29.4], write a function list_report(data) that 
prints: min, max, sum, average(all computed with loops — no built-ins), 
and whether the list is sorted ascending. Add a docstring.
'''

temps = [22.5, 31.0, 18.3, 27.8, 35.1, 20.0, 29.4]
def list_report(data):
    """Finds min,max,sum and average of a list"""
    minimum = data[0]
    maximum = data[0]
    total = 0
    for item in data:
        if item < minimum:
            minimum = item
    print("Minimum:",minimum)  

    for item in data:
        if item > maximum:
            maximum = item
    print("Maximum:",maximum)        

    for item in data:
        total+=item
    print("Total:",total)

    average = total/len(data)    
    print("Average:",average)

print(list_report.__doc__)
print(temps)    
list_report(temps)