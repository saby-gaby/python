team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sequence_of_cards = input().split()
is_game_terminated = False
for card in sequence_of_cards:
    curr_card = card.split('-')
    team = curr_card[0]
    player = int(curr_card[1])
    if team == 'A' and player in team_a:
        team_a.remove(player)
    elif team == 'B' and player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        is_game_terminated = True
        break
print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if is_game_terminated:
    print('Game was terminated')
