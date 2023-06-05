def print_result(command, given_input):
    result = None
    if command == 'int':
        result = int(given_input) * 2
    elif command == 'real':
        result = f'{float(given_input) * 1.5:.2f}'
    elif command == 'string':
        result = f'${given_input}$'
    return print(result)


user_command = input()
user_input = input()
print_result(user_command, user_input)
