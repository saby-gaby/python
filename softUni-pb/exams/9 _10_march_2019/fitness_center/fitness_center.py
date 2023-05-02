clients = int(input())

training, protein = 0, 0
back, chest, legs, abs, shake, bar = 0, 0, 0, 0, 0, 0

for _ in range(clients):
    bought = input()

    if bought == 'Back':
        training += 1
        back += 1
    elif bought == 'Chest':
        training += 1
        chest += 1
    elif bought == 'Legs':
        training += 1
        legs += 1
    elif bought == 'Abs':
        training += 1
        abs += 1
    elif bought == 'Protein shake':
        protein += 1
        shake += 1
    elif bought == 'Protein bar':
        protein += 1
        bar += 1

training = training / clients * 100
protein = protein / clients * 100

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{shake} - protein shake')
print(f'{bar} - protein bar')
print(f'{training:.2f}% - work out')
print(f'{protein:.2f}% - protein')