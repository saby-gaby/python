number = int(input())

for num in range(1, number + 1):
    sum_digits = 0
    current_number = num
    while current_number > 0:
        sum_digits += current_number % 10
        current_number = int(current_number / 10)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
