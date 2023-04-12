max_value_first = int(input())
max_value_second = int(input())
max_value_last = int(input())

for digit1 in range(2, max_value_first + 1, 2):

    for digit2 in range(2, max_value_second + 1):

        if digit2 == 2 or digit2 == 3 or digit2 == 5 or digit2 == 7:
            pass
        else:
            continue

        for digit3 in range(2, max_value_last + 1, 2):
            print(digit1, digit2, digit3)
