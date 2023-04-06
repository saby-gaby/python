interval_min = int(input())
interval_max = int(input())
magic_number = int(input())

combinations = 0
is_found = False

for x in range(interval_min, interval_max + 1):

    for y in range(interval_min, interval_max + 1):
        combinations += 1

        if x + y == magic_number:
            is_found = True
            print(f'Combination N:{combinations} ({x} + {y} = {magic_number})')

    if is_found:
        break
else:
    print(f'{combinations} combinations - neither equals {magic_number}')
