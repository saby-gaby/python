n = int(input())
l = int(input())

for first_symbol in range(1, n + 1):
    for second_symbol in range(1, n + 1):

        for first_letter in range(97, 97 + l):
            for second_letter in range(97, 97 + l):
                if first_symbol > second_symbol:
                    last_symbol = first_symbol + 1
                else:
                    last_symbol = second_symbol + 1
                for _ in range(last_symbol, n + 1):
                    print(f'{first_symbol}{second_symbol}{chr(first_letter)}{chr(second_letter)}{last_symbol}', end=' ')
                    last_symbol += 1
