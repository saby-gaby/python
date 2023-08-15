cars_count = int(input())
garage = {}

for _ in range(cars_count):
    car, mileage, fuel = input().split('|')
    garage[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

command = input().split(' : ')
while command[0] != 'Stop':
    curr_command = command[0]
    if curr_command == 'Drive':
        curr_car, distance, fuel = command[1], int(command[2]), int(command[3])
        if fuel > garage[curr_car]['fuel']:
            print('Not enough fuel to make that ride')
        else:
            garage[curr_car]['fuel'] = garage[curr_car]['fuel'] - fuel
            garage[curr_car]['mileage'] = garage[curr_car]['mileage'] + distance
            print(f'{curr_car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if garage[curr_car]['mileage'] >= 100000:
            del garage[curr_car]
            print(f'Time to sell the {curr_car}!')
    elif curr_command == 'Refuel':
        curr_car, fuel = command[1], int(command[2])
        if 75 - garage[curr_car]['fuel'] < fuel:
            fuel = 75 - garage[curr_car]['fuel']
            garage[curr_car]['fuel'] = 75
        else:
            garage[curr_car]['fuel'] += fuel
        print(f'{curr_car} refueled with {fuel} liters')
    elif curr_command == 'Revert':
        curr_car, kilometers = command[1], int(command[2])
        garage[curr_car]['mileage'] -= kilometers
        print(f'{curr_car} mileage decreased by {kilometers} kilometers')
        if garage[curr_car]['mileage'] < 10000:
            garage[curr_car]['mileage'] = 10000
    command = input().split(' : ')

for vehicle, info in garage.items():
    print(f'{vehicle} -> Mileage: {info["mileage"]} kms, Fuel in the tank: {info["fuel"]} lt.')
