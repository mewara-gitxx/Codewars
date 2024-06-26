"""
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
"""

def find_smallest_int(arr):
    return min(arr)

"""
or

"""
def findSmallestInt(arr):
    smallest = 0
    for i in range(0,len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
    return smallest