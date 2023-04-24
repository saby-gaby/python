import sys

k_digit = int(input())
l_digit = int(input())
m_digit = int(input())
n_digit = int(input())

changes_counter = 0

for first in range(k_digit, 9):

    if first % 2 != 0:
        continue

    for second in range(9, l_digit - 1, -1):

        if second % 2 == 0:
            continue

        for third in range(m_digit, 9):

            if third % 2 != 0:
                continue

            for last in range(9, n_digit - 1, -1):

                if last % 2 == 0:
                    continue

                if first == third and second == last:
                    print('Cannot change the same player.')
                else:
                    print(f'{first}{second} - {third}{last}')
                    changes_counter += 1

                    if changes_counter == 6:
                        sys.exit()
