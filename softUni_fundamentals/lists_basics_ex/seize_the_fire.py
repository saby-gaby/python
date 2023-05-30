fires = input().split('#')
water = int(input())
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)
cells = []
for fire in fires:
    level_of_fire, value_of_fire = fire.split(' = ')
    value_of_fire = int(value_of_fire)
    if water >= value_of_fire:
        if (level_of_fire == 'High' and value_of_fire in high) or \
                (level_of_fire == 'Medium' and value_of_fire in medium) or \
                (level_of_fire == 'Low' and value_of_fire in low):
            water -= value_of_fire
            cells.append(value_of_fire)
print('Cells:')
for cell in cells:
    print(f' - {cell}')
print(f'Effort: {sum(cells) * 0.25:.2f}')
print(f'Total Fire: {sum(cells)}')
