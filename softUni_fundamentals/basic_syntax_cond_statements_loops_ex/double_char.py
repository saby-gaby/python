while True:
    current_string = input()
    if current_string == 'End':
        break
    elif current_string == 'SoftUni':
        continue
    new_string = ''
    for char in current_string:
        new_string += 2 * char
    print(new_string)
