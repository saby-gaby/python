encrypted_message = input()
command = input()
decrypted_message = ''
while command != 'Decode':
    if not decrypted_message:
        decrypted_message = encrypted_message
    curr_command = command.split('|')
    if curr_command[0] == 'Move':
        letters = int(curr_command[1])
        decrypted_message = decrypted_message[letters:] + decrypted_message[:letters]
    elif curr_command[0] == 'Insert':
        index = int(curr_command[1])
        value = curr_command[2]
        decrypted_message = decrypted_message[:index] + value + decrypted_message[index:]
    elif curr_command[0] == 'ChangeAll':
        decrypted_message = decrypted_message.replace(curr_command[1], curr_command[2])

    command = input()

print(f'The decrypted message is: {decrypted_message}')
