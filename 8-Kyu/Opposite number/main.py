"""
Very simple, given a number (integer / decimal / both depending on the language), 
find its opposite (additive inverse).
"""

def opposite(number):
    if number < 0:
        return abs(number)
    return -1 * number