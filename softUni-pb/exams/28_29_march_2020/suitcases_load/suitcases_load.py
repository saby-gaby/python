capacity = float(input())

counter, loaded = 0, 0

while True:
    suitcase = input()

    if suitcase == 'End':
        print('Congratulations! All suitcases are loaded!')
        break

    suitcase_volume = float(suitcase)
    counter += 1

    if counter % 3 == 0:
        suitcase_volume *= 1.1

    if capacity >= suitcase_volume:
        capacity -= suitcase_volume
        loaded += 1
    else:
        print('No more space!')
        break

print(f'Statistic: {loaded} suitcases loaded.')
