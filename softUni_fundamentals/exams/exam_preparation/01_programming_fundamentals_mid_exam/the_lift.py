people = int(input())
lift_state = [int(x) for x in input().split()]

for index, lift_space in enumerate(lift_state):
    free_places = 4 - lift_space
    if 0 < free_places <= people:
        people -= 4 - lift_space
        lift_state[index] = 4
    elif free_places > 0 and free_places > people:
        lift_state[index] += people
        people = 0
        break

lifts = ' '.join(map(lambda x: str(x), lift_state))

if people:
    print(f'There isn\'t enough space! {people} people in a queue!')
elif people == 0 and lift_state[-1] < 4:
    print(f'The lift has empty spots!')
print(lifts)