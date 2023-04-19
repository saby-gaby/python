from math import ceil

num = int(input())

for row in range(1, num + 1):
    if row == 1 or row == num:
        print(2 * num * '*' + num * ' ' + 2 * num * '*')
    elif (num % 2 != 0 and row == ceil(num / 2)) or (num % 2 == 0 and row == num / 2):
        print('*' + (2 * num - 2) * '/' + '*' + num * '|' + '*' + (2 * num - 2) * '/' + '*')
    else:
        print('*' + (2 * num - 2) * '/' + '*' + num * ' ' + '*' + (2 * num - 2) * '/' + '*')
