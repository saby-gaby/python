start_interval = input()
end_interval = input()

for first in range(int(start_interval[0]), int(end_interval[0]) + 1):
    if first % 2 == 0:
        continue

    for second in range(int(start_interval[1]), int(end_interval[1]) + 1):
        if second % 2 == 0:
            continue

        for third in range(int(start_interval[2]), int(end_interval[2]) + 1):
            if third % 2 == 0:
                continue

            for last in range(int(start_interval[3]), int(end_interval[3]) + 1):
                if last % 2 == 0:
                    continue

                print(f'{first}{second}{third}{last}', end=' ')
