while True:
    destination = input()

    if destination == 'End':
        break

    needed_money = float(input())
    saved_money = 0

    while True:
        saved_money += float(input())

        if saved_money >= needed_money:
            print(f'Going to {destination}!')
            break
