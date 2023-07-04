parking = {}
number_of_commands = int(input())

for _ in range(number_of_commands):
    user_input = input().split()
    command = user_input[0]
    user = user_input[1]

    if command == 'register':
        plate_number = user_input[2]
        if user in parking:
            print(f'ERROR: already registered with plate number {plate_number}')
        else:
            parking[user] = plate_number
            print(f'{user} registered {plate_number} successfully')
    elif command == 'unregister':
        if user in parking:
            print(f'{user} unregistered successfully')
            parking.pop(user)
        else:
            print(f'ERROR: user {user} not found')

for user, plate in parking.items():
    print(f'{user} => {plate}')
