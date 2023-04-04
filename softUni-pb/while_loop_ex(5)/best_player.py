best_player = ''
most_goals = -1

while most_goals < 10:
    player = input()

    if player == 'END':
        break

    goals = int(input())

    if goals > most_goals:
        best_player = player
        most_goals = goals

print(f'{best_player} is the best player!')
print(f"He has scored {most_goals} goals{' and made a hat-trick !!!' if most_goals >= 3 else '.'}")

