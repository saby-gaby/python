import sys

a = int(input())
b = int(input())
max_passwords = int(input())

password_counter = 0
symbol_a = 35
symbol_b = 64
password = ''


for x in range(1, a + 1):
    for y in range(1, b + 1):

        if symbol_a > 55:
            symbol_a = 35

        if symbol_b > 96:
            symbol_b = 64

        password = chr(symbol_a) + chr(symbol_b) + str(x) + str(y) + chr(symbol_b) + chr(symbol_a)

        print(f'{password}', end='|')

        password_counter += 1
        symbol_a += 1
        symbol_b += 1

        if password_counter >= max_passwords:
            sys.exit()
