tournament_days = int(input())
money, days_won, days_lose = 0, 0, 0

for day in range(tournament_days):
    daily_money = 0
    wins, loses = 0, 0

    while True:
        game = input()

        if game == 'Finish':
            break

        result = input()

        if result == 'win':
            wins += 1
            daily_money += 20
        elif result == 'lose':
            loses += 1

    if wins > loses:
        days_won += 1
    else:
        days_lose += 1

    if wins > loses:
        daily_money *= 1.1

    money += daily_money


if days_lose < days_won:
    money *= 1.2
    print(f'You won the tournament! Total raised money: {money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {money:.2f}')
