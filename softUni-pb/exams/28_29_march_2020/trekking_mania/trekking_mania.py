groups_count = int(input())

total_climbers, musala, monblan, kilimandjaro, k2, everest = 0, 0, 0, 0, 0, 0

for _ in range(groups_count):
    climbers = int(input())
    total_climbers += climbers

    if climbers < 6:
        musala += climbers
    elif climbers <= 12:
        monblan += climbers
    elif climbers <= 25:
        kilimandjaro += climbers
    elif climbers <= 40:
        k2 += climbers
    else:
        everest += climbers

print(f'{musala  / total_climbers * 100:.2f}%')
print(f'{monblan / total_climbers * 100:.2f}%')
print(f'{kilimandjaro / total_climbers * 100:.2f}%')
print(f'{k2 / total_climbers * 100:.2f}%')
print(f'{everest / total_climbers * 100:.2f}%')
