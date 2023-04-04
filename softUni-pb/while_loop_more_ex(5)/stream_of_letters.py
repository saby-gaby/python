message = ''
word = ''

is_n = False
is_o = False
is_c = False


while True:
    letter = input()

    if letter == 'End':
        print(message)
        break

    if (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122):

        if letter == 'n' and not is_n:
            is_n = True
        elif letter == 'o' and not is_o:
            is_o = True
        elif letter == 'c' and not is_c:
            is_c = True
        else:
            word += letter

        if is_n and is_c and is_o:
            message += word + ' '
            word = ''
            is_n = False
            is_o = False
            is_c = False
    else:
        continue

