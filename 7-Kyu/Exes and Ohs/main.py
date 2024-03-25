"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""
def xo(s):
    simplify = s.lower()
    num_x = 0
    num_o = 0
    for letter in range(len(simplify)):
        if simplify[letter] == 'x':
            num_x += 1
        elif simplify[letter] == 'o':
            num_o += 1
    if num_x == num_o:
        return True
    else:
        return False
    

"""
Another way
"""
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')