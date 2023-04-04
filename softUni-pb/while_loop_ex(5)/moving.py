free_volume = int(input()) * int(input()) * int(input())

while free_volume > 0:
    boxes = input()

    if boxes == 'Done':
        print(f'{free_volume} Cubic meters left.')
        break
    else:
        free_volume -= int(boxes)
else:
    print(f'No more free space! You need {abs(free_volume)} Cubic meters more.')
