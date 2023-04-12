min_num = int(input())
max_num = int(input())

for first in range(min_num, max_num + 1):

    for second in range(min_num, max_num + 1):

        for third in range(min_num, max_num + 1):

            for last in range(min_num, max_num + 1):

                if first > last and \
                        (second + third) % 2 == 0 and \
                        ((first % 2 == 0 and last % 2 != 0) or (first % 2 != 0 and last % 2 == 0)):
                    print(f'{first}{second}{third}{last}', end=' ')
