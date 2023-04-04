detergent = int(input()) * 750

cycle = 0
plates = 0
pots = 0

while detergent >= 0:
    user_input = input()

    if user_input == 'End':
        print('Detergent was enough!')
        print(f'{plates} dishes and {pots} pots were washed.')
        print(f'Leftover detergent {detergent} ml.')
        break

    dishes = int(user_input)
    cycle += 1

    if cycle % 3 == 0:
        pots += dishes
        detergent -= dishes * 15
    else:
        plates += dishes
        detergent -= dishes * 5
else:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
