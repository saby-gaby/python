def check_the_rooms(count_rooms):
    free_chairs = 0
    for room in range(1, count_rooms + 1):
        chairs, visitors = input().split()
        diff = len(chairs) - int(visitors)
        if diff < 0:
            print(f'{abs(diff)} more chairs needed in room {room}')
        free_chairs += diff

    return free_chairs


rooms_count = int(input())
total_free_chairs = check_the_rooms(rooms_count)
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')
