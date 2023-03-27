num1 = int(input())
num2 = int(input())
operator = input()
res = None

if operator == '+':
    res = f'{num1} {operator} {num2} = {num1 + num2}' + (' - even' if (num1 + num2) % 2 == 0 else ' - odd')
    # if (num1 + num2) % 2 == 0:
    #     res += ' - even'
    # else:
    #     res += ' - odd'
elif operator == '-':
    res = f'{num1} {operator} {num2} = {num1 - num2}' + (' - even' if (num1 - num2) % 2 == 0 else ' - odd')
elif operator == '*':
    res = f'{num1} {operator} {num2} = {num1 * num2}' + (' - even' if (num1 * num2) % 2 == 0 else ' - odd')
elif num2 == 0:
    res = f'Cannot divide {num1} by zero'
elif operator == '/':
    res = f'{num1} / {num2} = {num1 / num2:.2f}'
elif operator == '%':
    res = f'{num1} % {num2} = {num1 % num2}'

print(res)
