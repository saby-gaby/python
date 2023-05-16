total_coffees = 0
while True:
    command = input()
    if command == 'END':
        break

    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        total_coffees += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        total_coffees += 2
    else:
        continue

if total_coffees > 5:
    print('You need extra sleep')
else:
    print(total_coffees)
