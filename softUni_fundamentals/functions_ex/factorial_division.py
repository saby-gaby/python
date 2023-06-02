def factorial(num):
    result = 1
    for current_num in range(2, num + 1):
        result *= current_num
    return result


def get_factorial(first, second):
    first_factorial = factorial(first)
    second_factorial = factorial(second)
    return f'{first_factorial / second_factorial:.2f}'


first_num = int(input())
second_num = int(input())
print(get_factorial(first_num, second_num))
