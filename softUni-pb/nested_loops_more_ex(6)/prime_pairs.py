first_min = int(input())
second_min = int(input())
first_max = int(input()) + first_min
second_max = int(input()) + second_min

first_counter, second_counter = 0, 0

for first_half in range(first_min, first_max + 1):
    for i in range(2, first_half):
        if first_half % i == 0:
            if first_counter == 0:
                first_counter += 1
                break

    if first_counter == 0:

        for second_half in range(second_min, second_max + 1):
            for j in range(2, second_half):
                if second_half % j == 0:
                    if second_counter == 0:
                        second_counter += 1
                        break

            if second_counter == 0:
                print(f'{first_half}{second_half}')
            else:
                second_counter = 0
                continue
    else:
        first_counter = 0
        continue
