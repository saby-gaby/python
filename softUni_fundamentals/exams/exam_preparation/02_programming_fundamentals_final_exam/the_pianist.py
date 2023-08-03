number_pieces = int(input())
favorites = {}

for _ in range(number_pieces):
    curr_piece = input().split('|')
    favorites[curr_piece[0]] = {'composer': curr_piece[1], 'key': curr_piece[2]}

command = input()
while command != 'Stop':
    curr_command = command.split('|')
    curr_piece = curr_command[1]
    if curr_command[0] == 'Add':
        if curr_piece in favorites.keys():
            print(f'{curr_piece} is already in the collection!')
        else:
            favorites[curr_piece] = {'composer': curr_command[2], 'key': curr_command[3]}
            print(f'{curr_piece} by {favorites[curr_piece]["composer"]} in {favorites[curr_piece]["key"]} added to the collection!')
    elif curr_command[0] == 'Remove':
        if curr_piece in favorites.keys():
            favorites.pop(curr_piece)
            print(f'Successfully removed {curr_piece}!')
        else:
            print(f'Invalid operation! {curr_piece} does not exist in the collection.')
    elif curr_command[0] == 'ChangeKey':
        if curr_piece in favorites.keys():
            favorites[curr_piece]['key'] = curr_command[2]
            print(f'Changed the key of {curr_piece} to {curr_command[2]}!')
        else:
            print(f'Invalid operation! {curr_piece} does not exist in the collection.')

    command = input()
for piece, info in favorites.items():
    print(f'{piece} -> Composer: {info["composer"]}, Key: {info["key"]}')
