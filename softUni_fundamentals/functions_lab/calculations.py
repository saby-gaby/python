def calculator(operator, first, second):
    if operator == 'multiply':
        return first * second
    elif operator == 'divide':
        return first // second
    elif operator == 'add':
        return first + second
    elif operator == 'subtract':
        return first - second


operator_input = input()
first_integer = int(input())
second_integer = int(input())
print(calculator(operator_input, first_integer, second_integer))
