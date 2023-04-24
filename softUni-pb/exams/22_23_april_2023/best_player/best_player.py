best_player = ''
most_goals = 0

while True:
    current_player = input()

    if current_player == 'END':
        break

    goals = int(input())

    if goals > most_goals:
        best_player = current_player
        most_goals = goals

    if goals >= 10:
        break

message = 'He has scored ' + str(most_goals) + ' goals'
message_end = ' and made a hat-trick !!!' if most_goals >= 3 else '.'

print(f'{best_player} is the best player!')
print(message + message_end)
