points = int(input())
# bonus_points = 0  # rows 4 - 9 cover all possibilities and bonus_points will be created, so here we don't need that

if points <= 100:
    bonus_points = 5
elif points > 1000:
    bonus_points = points * 0.1
else:
    bonus_points = points * 0.2

if points % 2 == 0:
    bonus_points += 1
elif points % 10 == 5:
    bonus_points += 2

total_points = points + bonus_points

print(f'{bonus_points}\n{total_points}')
