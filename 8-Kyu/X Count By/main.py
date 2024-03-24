"""
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.
"""
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return list(range(x,x*n+1,x))