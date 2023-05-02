from math import floor

tournaments_count = int(input())
start_points = int(input())

tournaments_won = 0
tournaments_points = 0

for _ in range(tournaments_count):
    tournament_stage = input()

    if tournament_stage == 'W':
        tournaments_won += 1
        tournaments_points += 2000
    elif tournament_stage == 'F':
        tournaments_points += 1200
    elif tournament_stage == 'SF':
        tournaments_points += 720

average_points = tournaments_points / tournaments_count
tournaments_won = tournaments_won / tournaments_count * 100

print(f'Final points: {floor(start_points + tournaments_points)}')
print(f'Average points: {floor(average_points)}')
print(f'{tournaments_won:.2f}%')
