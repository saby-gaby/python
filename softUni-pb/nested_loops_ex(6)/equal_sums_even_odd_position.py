min_num = int(input())
max_num = int(input())

for number in range(min_num, max_num + 1):
    num_to_str = str(number)
    sum_odd = 0
    sum_even = 0

    for i, digit in enumerate(num_to_str):
        if i % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_odd == sum_even:
        print(f'{number}', end=' ')
