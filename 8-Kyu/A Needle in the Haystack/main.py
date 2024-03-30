"""
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle,

"""
def find_needle(haystack):
    # your code here
    if 'needle' in haystack:
        return f'found the needle at position {haystack.index('needle')}'
    