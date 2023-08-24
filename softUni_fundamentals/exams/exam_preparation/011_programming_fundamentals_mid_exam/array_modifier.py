array = [int(num) for num in input().split()]

while True:
    command = input().split()
    if command[0] == 'end':
        break
    if command[0] == 'swap':
        index_1, index_2 = int(command[1]), int(command[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif command[0] == 'multiply':
        index_1, index_2 = int(command[1]), int(command[2])
        array[index_1] = array[index_1] * array[index_2]
    elif command[0] == 'decrease':
        array = [num - 1 for num in array]

print(*array, sep=', ')
