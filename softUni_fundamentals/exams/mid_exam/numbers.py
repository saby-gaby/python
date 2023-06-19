numbers = [int(x) for x in input().split()]

while True:
    command = input()
    if command == 'Finish':
        break
    command = command.split()
    if command[0] == 'Add':
        numbers.append(int(command[1]))
    elif command[0] == 'Remove':
        if int(command[1]) in numbers:
            index_of_number = numbers.index(int(command[1]))
            numbers.pop(index_of_number)
    elif command[0] == 'Replace' :
        if int(command[1]) in numbers:
            index_of_number = numbers.index(int(command[1]))
            numbers[index_of_number] = int(command[2])
    elif command[0] == 'Collapse' :
        numbers = [x for x in numbers if x >= int(command[1])]

print(*numbers, sep=' ')