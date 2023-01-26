count = int(input())
odd_sum, odd_min, odd_max, even_sum, even_min, even_max = 0, 0, 0, 0, 0, 0

for pos in range(1, count + 1):
    num = float(input())

    if pos % 2 != 0:
        odd_sum += num

        if odd_min == 0:
            odd_min = num
        elif odd_min > num:
            odd_min = num
        if odd_max == 0:
            odd_max = num
        elif odd_max < num:
            odd_max = num
    else:
        even_sum += num

        if even_min == 0:
            even_min = num
        elif even_min > num:
            even_min = num
        if even_max == 0:
            even_max = num
        elif even_max < num:
            even_max = num

print(f'OddSum={odd_sum:.2f},')

if odd_sum == 0:
    print('OddMin=No,')
    print('OddMax=No,')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')

if even_sum == 0:
    print('EvenMin=No,')
    print('EvenMax=No')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')
