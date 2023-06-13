wagons_count = int(input())
command = input()
train = [0] * wagons_count

while command != 'End':
    command = command.split()
    curr_command = command[0]
    if curr_command == 'add':
        train[-1] += int(command[1])
    else:
        index, count = int(command[1]), int(command[2])
        if curr_command == 'insert':
            train[index] += count
        elif curr_command == 'leave':
            train[index] -= count

    command = input()

print(train)
