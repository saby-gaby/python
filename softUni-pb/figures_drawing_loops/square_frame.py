num = int(input())

for i in range(1, num + 1):
    if i == 1 or i == num:
        print('+ ' + '- ' * (num - 2) + '+')
    else:
        print('| ' + '- ' * (num - 2) + '|')
