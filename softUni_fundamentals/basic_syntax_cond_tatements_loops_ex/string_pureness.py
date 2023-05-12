count_strings = int(input())

for _ in range(count_strings):
    current_string = input()
    is_str_clean = True
    for char in current_string:
        if char == ',' or char == '.' or char == '_':
            is_str_clean = False
            break
    if is_str_clean:
        print(f'{current_string} is pure.')
    else:
        print(f'{current_string} is not pure!')
