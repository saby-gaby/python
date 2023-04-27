player_name = input()

player_points = 301
successful_attempts, unsuccessful_attempts = 0, 0

while True:
    field = input()

    if field == 'Retire':
        print(f'{player_name} retired after {unsuccessful_attempts} unsuccessful shots.')
        break

    points = int(input())

    if field == 'Double':
        points *= 2
    elif field == 'Triple':
        points *= 3

    if player_points >= points:
        player_points -= points
        successful_attempts += 1
    else:
        unsuccessful_attempts += 1

    if player_points == 0:
        print(f'{player_name} won the leg with {successful_attempts} shots.')
        break
