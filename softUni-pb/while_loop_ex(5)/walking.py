goal = 10000
steps = 0

while steps < goal:
    log = input()

    if log == 'Going home':
        steps += int(input())
        if steps < goal:
            print(f'{goal - steps} more steps to reach goal.')
            break
    else:
        steps += int(log)
else:
    print(f'Goal reached! Good job!\n{steps - goal} steps over the goal!')
