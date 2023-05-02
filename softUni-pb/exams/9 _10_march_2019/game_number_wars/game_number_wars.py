first_player_name = input()
second_player_name = input()

first_player_points, second_player_points = 0, 0
is_number_wars = False

while True:
    first_player_card = input()

    if first_player_card == 'End of game':
        print(f'{first_player_name} has {first_player_points} points')
        print(f'{second_player_name} has {second_player_points} points')
        break

    first_player_card = int(first_player_card)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        if is_number_wars:
            print(f'{first_player_name} is winner with {first_player_points} points')
            break

        first_player_points += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        if is_number_wars:
            print(f'{second_player_name} is winner with {second_player_points} points')
            break

        second_player_points += second_player_card - first_player_card
    else:
        is_number_wars = True
        print('Number wars!')
