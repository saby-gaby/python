budget = int(input())
command = input()

while command != 'End':
    price = int(command)
    if price > budget:
        print('You went in overdraft!')
        break
    else:
        budget -= price

    command = input()
else:
    print('You bought everything needed.')
