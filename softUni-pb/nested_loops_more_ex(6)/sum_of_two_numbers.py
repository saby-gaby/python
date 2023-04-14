import sys

start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

counter = 0

for first_digit in range(start_interval, end_interval + 1):

    for second_digit in range(start_interval, end_interval + 1):
        counter += 1

        if first_digit + second_digit == magic_number:
            print(f'Combination N:{counter} ({first_digit} + {second_digit} = {magic_number})')
            sys.exit()
else:
    print(f'{counter} combinations - neither equals {magic_number}')