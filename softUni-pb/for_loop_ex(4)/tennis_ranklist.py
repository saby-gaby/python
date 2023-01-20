tournaments = int(input())
start_points = int(input())

points_earned = 0
won = 0

for _ in range(tournaments):
    tour_stage = input()

    if tour_stage == 'W':
        points_earned += 2000
        won += 1
    elif tour_stage == 'F':
        points_earned += 1200
    elif tour_stage == 'SF':
        points_earned += 720

print(f'Final points: {start_points + points_earned}')
print(f'Average points: {int(points_earned / tournaments)}')
print(f'{won / tournaments * 100:.2f}%')
