raw_key = input()
activation_key = ''

while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        break
    if not activation_key:
        activation_key = raw_key
    if command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        curr_command, start, end = command[1], int(command[2]), int(command[3])
        if curr_command == 'Upper':
            activation_key = activation_key[:start] + activation_key[start:end].upper() + activation_key[end:]
        elif curr_command == 'Lower':
            activation_key = activation_key[:start] + activation_key[start:end].lower() + activation_key[end:]
        print(activation_key)
    elif command[0] == 'Slice':
        start, end = int(command[1]), int(command[2])
        activation_key = activation_key[:start] + activation_key[end:]
        print(activation_key)
print(f'Your activation key is: {activation_key}')
