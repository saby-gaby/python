num = int(input())

for first in range(1, num + 1):

    if first >= 10:
        break

    for second in range(1, num + 1):

        if second >= 10:
            break

        for third in range(1, num + 1):

            if third >= 10:
                break

            for last in range(1, num + 1):

                if last >= 10:
                    break

                if num % (first + second) == 0 and first + second == third + last:
                    print(f'{first}{second}{third}{last}', end=' ')
