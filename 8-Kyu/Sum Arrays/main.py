"""
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. 
If the array does not contain any numbers then you should return 0.
"""

def sum_array(a):
    if len(a) == 0:
        return 0
    else:
        return sum(a)