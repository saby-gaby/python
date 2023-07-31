user_password = input()
command = input()

while command != 'Complete':
    curr_command = command.split()
    if len(curr_command) == 3:
        if curr_command[0] == 'Make':
            i = int(curr_command[2])
            if curr_command[1] == 'Upper':
                if i in range(len(user_password)):
                    user_password = user_password.replace(user_password[i], user_password[i].upper(), 1)
                    print(user_password)
            elif curr_command[1] == 'Lower':
                if i in range(len(user_password)):
                    user_password = user_password.replace(user_password[i], user_password[i].lower(), 1)
                    print(user_password)
        elif curr_command[0] == 'Insert':
            i = int(curr_command[1])
            if i in range(len(user_password)):
                char = curr_command[2]
                user_password = user_password[:i] + char + user_password[i:]
                print(user_password)
        elif curr_command[0] == 'Replace':
            char = curr_command[1]
            if char in user_password:
                value = int(curr_command[2])
                new_char = chr(ord(char) + value)
                user_password = user_password.replace(char, new_char)
                print(user_password)
    elif len(curr_command) == 1:
        if curr_command[0] == 'Validation':
            if len(user_password) < 8:
                print('Password must be at least 8 characters long!')
            has_only_valid_chars = True
            has_digit = False
            for char in user_password:
                if char != '_' and not char.isalnum() and has_only_valid_chars:
                    has_only_valid_chars = False
                if char.isdigit() and not has_digit:
                    has_digit = True
            if not has_only_valid_chars:    # elif not all('a' <= c.lower() <= 'z' or '0' <= c <= '9' or c == '_' for c in password):
                print('Password must consist only of letters, digits and _!')
            if user_password.islower():
                print('Password must consist at least one uppercase letter!')
            if user_password.isupper():
                print('Password must consist at least one lowercase letter!')
            if not has_digit:
                print('Password must consist at least one digit!')


    command = input()





# def check_password(password):
#     has_only_valid_chars = True
#     has_digit = False
#     if len(password) < 8:
#         return 'Password must be at least 8 characters long!'
#     for character in password:
#         if character.isalnum() or character == '_':
#             if character.isdigit() and not has_digit:
#                 has_digit = True
#         else:
#             has_only_valid_chars = False
#
#     if not has_only_valid_chars:
#         return 'Password must consist only of letters, digits and _!'
#     if user_wanted_psw.lower():
#         return 'Password must consist at least one uppercase letter!'
#     if user_wanted_psw.isupper():
#         return 'Password must consist at least one lowercase letter!'
#     if not has_digit:
#         return 'Password must consist at least one digit!'
#
#
# user_wanted_psw = input()
# command = input().split()
#
# while command[0] != 'Complete':
#      if len(command) == 3:
#          if command[0] == 'Make':
#              if command[1] == 'Upper':
#                  index = int(command[2])
#                  if index in range(len(user_wanted_psw)):
#                      user_wanted_psw = user_wanted_psw.replace(user_wanted_psw[index], user_wanted_psw[index].upper(), 1)
#                      print(user_wanted_psw)
#              elif command[1] == 'Lower':
#                  index = int(command[2])
#                  if index in range(len(user_wanted_psw)):
#                      user_wanted_psw = user_wanted_psw.replace(user_wanted_psw[index], user_wanted_psw[index].lower(), 1)
#                      print(user_wanted_psw)
#          elif command[0] == 'Insert':
#             index = int(command[1])
#             if index in range(len(user_wanted_psw)):
#                 char = command[2]
#                 user_wanted_psw = user_wanted_psw[:index] + char + user_wanted_psw[index:]
#                 print(user_wanted_psw)
#          elif command[0] == 'Replace':
#              char = command[1]
#              if char in user_wanted_psw:
#                  value = int(command[2])
#                  new_value = ord(char) + value
#                  new_char = chr(new_value)
#                  user_wanted_psw = user_wanted_psw.replace(char, new_char)
#                  print(user_wanted_psw)
#      elif len(command) == 1:
#          if command[0] == 'Validation':
#              validation_result = check_password(user_wanted_psw)
#              if validation_result:
#                 print(validation_result)
#
#      command = input().split()
