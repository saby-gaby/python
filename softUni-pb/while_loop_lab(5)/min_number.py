min_num = int(input())

while True:
    curr_num = input()

    if curr_num == 'Stop':
        break
    else:
        curr_num = int(curr_num)

        if min_num > curr_num:
            min_num = curr_num

print(min_num)
