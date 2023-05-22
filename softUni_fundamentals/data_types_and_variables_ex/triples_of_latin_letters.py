number_symbols = int(input())

for first in range(number_symbols):
    for second in range(number_symbols):
        for third in range(number_symbols):
            print(chr(97 + first) + chr(97 + second) + chr(97 + third))
