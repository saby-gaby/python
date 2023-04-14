max_hundred = int(input())
max_tens = int(input())
max_ones = int(input())

for hundred in range(2, max_hundred + 1, 2):

    for ten in range(2, max_tens + 1):
        if ten == 2 or ten == 3 or ten == 5 or ten == 7:
            pass
        else:
            continue

        for unit in range(2, max_ones + 1, 2):
            print(hundred, ten, unit)
