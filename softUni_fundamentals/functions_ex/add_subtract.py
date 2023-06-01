def sum_numbers(first, second):
    return first + second


def subtract(first_two_sum, third):
    return first_two_sum - third


def add_and_subtract(first, second, third):
    first_sum = sum_numbers(first, second)
    result = subtract(first_sum, third)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
