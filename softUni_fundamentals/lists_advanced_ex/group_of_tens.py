def print_groups(numbers):
    group = 0

    while numbers:
        group += 10
        curr_group = [curr for curr in numbers if curr <= group]
        print(f'Group of {group}\'s: {curr_group}')
        numbers = [curr for curr in numbers if curr not in curr_group]

numbers_list = list(map(int, input().split(', ')))
print_groups(numbers_list)
