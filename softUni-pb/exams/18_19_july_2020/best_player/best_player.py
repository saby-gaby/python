best_player = ''
most_goals = 0

while True:
    current_player = input()

    if current_player == 'END':
        break

    current_goals = int(input())

    if current_goals >= 10:
        best_player = current_player
        most_goals = current_goals
        break

    if not best_player:
        best_player = current_player
        most_goals = current_goals
    elif current_goals > most_goals:
        best_player = current_player
        most_goals = current_goals

message = 'He has scored ' + str(most_goals) + ' goals'
message += ' and made a hat-trick !!!' if most_goals >= 3 else '.'

print(f'{best_player} is the best player!')
print(message)
