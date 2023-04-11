special_num = int(input())

for number in range(1111, 10000):
    num = ''
    for digit in str(number):
        if int(digit) > 0 and special_num % int(digit) == 0:
            num += digit
        else:
            continue
    if len(num) == 4:
        print(f'{int(num)}', end=' ')
