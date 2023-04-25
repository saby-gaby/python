won, lost, equal = 0, 0, 0

for _ in range(3):
    game_result = input()

    if int(game_result[0]) == int(game_result[2]):
        equal += 1
    elif int(game_result[0]) > int(game_result[2]):
        won += 1
    else:
        lost += 1

print(f'Team won {won} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {equal}')
