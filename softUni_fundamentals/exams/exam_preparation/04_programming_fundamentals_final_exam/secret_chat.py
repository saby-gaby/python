message = input()
command = input()

while command != 'Reveal':
    command = command.split(':|:')
    curr_command = command[0]
    if curr_command == 'InsertSpace':
        index = int(command[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif curr_command == 'Reverse':
        if command[1] in message:
            new_substring = command[1][::-1]
            index = message.index(command[1])
            message = message[:index] + message[index + len(command[1]):] + new_substring
            print(message)
        else:
            print('error')
    elif curr_command == 'ChangeAll':
        if command[1] in message:
            message = message.replace(command[1], command[2])
            print(message)
    command = input()

print(f'You have a new text message: {message}')
