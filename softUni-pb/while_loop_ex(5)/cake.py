cake_width = int(input())
cake_length = int(input())
cake_pieces = cake_length * cake_width

while cake_pieces > 0:
    taken_pieces = input()

    if taken_pieces == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break
    else:
        cake_pieces -= int(taken_pieces)
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
