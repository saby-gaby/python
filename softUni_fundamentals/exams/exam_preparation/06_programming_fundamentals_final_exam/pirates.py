targets = {}

while True:
    command = input().split('||')
    if command[0] == 'Sail':
        break
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in targets.keys():
        targets[city] = {'population': population, 'gold': gold}
    else:
        targets[city]['population'] += population
        targets[city]['gold'] += gold
while True:
    command = input().split('=>')
    if command[0] == 'End':
        break
    curr_command, town = command[0], command[1]
    if curr_command == 'Plunder':
        people, gold = int(command[2]), int(command[3])
        targets[town]['population'] -= people
        targets[town]['gold'] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if not targets[town]['population'] or not targets[town]['gold']:
            del targets[town]
            print(f'{town} has been wiped off the map!')
    elif curr_command == 'Prosper':
        gold = int(command[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
            continue
        targets[town]['gold'] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {targets[town]["gold"]} gold.')
if targets:
    print(f'Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:')
    for town, details in targets.items():
        print(f'{town} -> Population: {details["population"]} citizens, Gold: {details["gold"]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
