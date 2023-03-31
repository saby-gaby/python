max_num = 0

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    else:
        curr_num = int(user_input)

        if max_num == 0:
            max_num = curr_num
        if max_num < curr_num:
            max_num = curr_num

print(max_num)
