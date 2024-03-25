"""

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

def add_binary(a,b):
    sum = a + b
    binary_str = format(int(sum), 'b')
    return binary_str

"""
# format the integer to binary
binary_value = format(value, 'b') #returns string
"""
