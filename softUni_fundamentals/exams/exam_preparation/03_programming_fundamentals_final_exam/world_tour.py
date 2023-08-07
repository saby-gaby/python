stops = input()

command = input()
while command != 'Travel':
    command = command.split(':')
    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
    elif command[0] == 'Remove Stop':
        start_i, end_i = int(command[1]), int(command[2])
        if start_i in range(len(stops)) and end_i in range(len(stops)):
            stops = stops[:start_i] + stops[end_i + 1:]
    elif command[0] == 'Switch':
        old_str, new_str = command[1], command[2]
        if old_str in stops:
            stops = stops.replace(old_str, new_str)
    print(stops)

    command = input()

print(f'Ready for world tour! Planned stops: {stops}')
