"""
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

"""
def get_grade(s1, s2, s3):
    avg_s = (s1 + s2 + s3) / 3
    if avg_s <=100 and avg_s >= 90:
        return 'A'
    elif avg_s < 90 and avg_s >= 80:
        return 'B'
    elif avg_s < 80 and avg_s >= 70:
        return 'C'
    elif avg_s < 70 and avg_s >= 60:
        return 'D'
    else:
        return "F"

def get_grade(s1, s2, s3):
    mean = sum([s1,s2,s3])/3
    if mean>=90: return 'A'
    if mean>=80: return 'B'
    if mean>=70: return 'C'
    if mean>=60: return 'D'
    return 'F'
