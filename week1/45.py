'''List Slicer
Given nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use slicing to print:
First 4 elements
Last 3 elements
Elements from index 2 to 6
Every other element
The entire list reversed
'''
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[:4])
print(nums[7:])
print(nums[2:7])
print(nums[::2])
nums.reverse()
print(nums)