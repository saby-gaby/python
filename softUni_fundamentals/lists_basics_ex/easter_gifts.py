gifts = input().split()
command = input()
result_lst = []
while command != 'No Money':
    command_lst = command.split()
    if command_lst[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command_lst[1]:
                gifts[i] = 'None'
    elif command_lst[0] == 'Required':
        if 0 <= int(command_lst[2]) < len(gifts):
            gifts[int(command_lst[2])] = command_lst[1]
    elif command_lst[0] == 'JustInCase':
        gifts[-1] = command_lst[1]
    command = input()
bought_gifts = [gift for gift in gifts if gift != 'None']
print(' '.join(bought_gifts))
