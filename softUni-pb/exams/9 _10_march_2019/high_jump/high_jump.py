target_height = int(input())

current_height = target_height - 30
is_jumped = False
counter_jumps = 0

while True:

    for _ in range(3):
        jumped = int(input())
        counter_jumps += 1

        if jumped > current_height:
            current_height += 5
            break
    else:
        break

    if current_height > target_height:
        is_jumped = True
        break

if is_jumped:
    print(f'Tihomir succeeded, he jumped over {current_height - 5}cm after {counter_jumps} jumps.')
else:
    print(f'Tihomir failed at {current_height}cm after {counter_jumps} jumps.')
