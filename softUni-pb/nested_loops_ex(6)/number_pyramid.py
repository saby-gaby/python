number = int(input())
current = 0

for i in range(1, number + 1):
    for j in range(1, i + 1):
        current += 1

        if j == i:
            print(f'{current}')
        else:
            print(f'{current}', end=' ')
        if current == number:
            raise SystemExit
    #         break
    #
    # if current == number:
    #     break
