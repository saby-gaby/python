capacity = int(input())
fans = int(input())
a_sector, b_sector, v_sector, g_sector = 0, 0, 0, 0

for _ in range(fans):
    sector = input()

    if sector == 'A':
        a_sector += 1
    elif sector == 'B':
        b_sector += 1
    elif sector == 'V':
        v_sector += 1
    elif sector == 'G':
        g_sector += 1

print(f'{a_sector / fans * 100:.2f}%')
print(f'{b_sector / fans * 100:.2f}%')
print(f'{v_sector / fans * 100:.2f}%')
print(f'{g_sector / fans * 100:.2f}%')
print(f'{fans / capacity * 100:.2f}%')
