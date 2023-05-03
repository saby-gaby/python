matches_won = 0
matches_lose = 0

while True:
    tournament_name = input()

    if tournament_name == 'End of tournaments':
        break

    games = int(input())
    for game in range(1, games + 1):
        team_desi_points = int(input())
        opponent_team_points = int(input())

        if team_desi_points > opponent_team_points:
            matches_won += 1
            print(f'Game {game} of tournament {tournament_name}: win with {team_desi_points - opponent_team_points} \
points.')
        else:
            matches_lose += 1
            print(f'Game {game} of tournament {tournament_name}: lost with {opponent_team_points - team_desi_points} \
points.')

print(f'{matches_won / (matches_won + matches_lose) * 100:.2f}% matches win')
print(f'{matches_lose / (matches_won + matches_lose) * 100:.2f}% matches lost')
