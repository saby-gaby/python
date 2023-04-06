floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    room_type = ''
    floor_rooms = ''
    for room in range(rooms):
        if floor == floors:
            room_type = 'L'
        elif floor % 2 == 0:
            room_type = 'O'
        else:
            room_type = 'A'

        if not floor_rooms:
            floor_rooms = f'{room_type}{floor}{room}'
        else:
            floor_rooms += f' {room_type}{floor}{room}'

    print(floor_rooms)
