customers = int(input())

total_money = 0

for _ in range(customers):
    purchase = 0
    count_purchases = 0

    while True:
        item = input()

        if item == 'Finish':
            break
        elif item == 'basket':
            purchase += 1.5
        elif item == 'wreath':
            purchase += 3.8
        elif item == 'chocolate bunny':
            purchase += 7

        count_purchases += 1

    if count_purchases % 2 == 0:
        purchase *= 0.8

    total_money += purchase

    print(f'You purchased {count_purchases} items for {purchase:.2f} leva.')

print(f'Average bill per client is: {total_money / customers:.2f} leva.')
