string = input()
command = input()
password = ''

while command != 'Done':
    command = command.split(' ')
    curr_psw = []

    if not password:
        password += string

    if command[0] == 'TakeOdd':
        for i in range(1, len(password), 2):
            curr_psw.append(password[i])
        password = ''.join(curr_psw)
        print(password)
    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])
        substring = password[index: index + length]
        password = password.replace(substring, "", 1)
        print(password)
    elif command[0] == 'Substitute':
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')

    command = input()

print(f'Your password is: {password}')
