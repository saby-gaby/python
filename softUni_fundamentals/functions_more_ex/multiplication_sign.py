def check_positive_negative_or_zero(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return 'zero'
    if (num1 < 0 and (num2 > 0 and num3 > 0)) or \
            (num2 < 0 and (num1 > 0 and num3 > 0)) or \
            (num3 < 0 and (num1 > 0 and num2 > 0)) or \
            (num1 < 0 and num2 < 0 and num3 < 0):
        return 'negative'
    return 'positive'


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(check_positive_negative_or_zero(first_num, second_num, third_num))
