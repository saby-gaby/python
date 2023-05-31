def print_grade(grade_as_num):
    grade_as_word = ''
    if 2 <= grade_as_num < 3:
        grade_as_word = 'Fail'
    elif grade_as_num < 3.5:
        grade_as_word = 'Poor'
    elif grade_as_num < 4.5:
        grade_as_word = 'Good'
    elif grade_as_num < 5.5:
        grade_as_word = 'Very Good'
    else:
        grade_as_word = 'Excellent'
    print(grade_as_word)


grade = float(input())
print_grade(grade)
