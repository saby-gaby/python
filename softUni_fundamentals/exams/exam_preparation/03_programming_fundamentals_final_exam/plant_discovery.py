plant_count = int(input())
plants = {}

for _ in range(plant_count):
    plant = input().split('<->')
    plants[plant[0]] = {'rarity': int(plant[1])}

while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break
    plant_info = command[1].split(' - ')
    curr_plant = plant_info[0]
    if command[0] == 'Rate':
        if curr_plant in plants.keys():
            if 'rating' in plants[curr_plant].keys():
                plants[curr_plant]['rating'].append(int(plant_info[1]))
            else:
                plants[curr_plant]['rating'] = [int(plant_info[1])]
        else:
            print('error')
    elif command[0] == 'Update':
        if curr_plant in plants.keys():
            plants[curr_plant]['rarity'] = int(plant_info[1])
        else:
            print('error')
    elif command[0] == 'Reset':
        if curr_plant in plants.keys() and plants[curr_plant]['rating']:
            plants[curr_plant].pop('rating')
        else:
            print('error')
print('Plants for the exhibition:')
for plant, info in plants.items():
    if 'rating' in info:
        avg_rating = f'{sum(info["rating"]) / len(info["rating"]):.2f}'
    else:
        avg_rating = f'{0:.2f}'
    print(f'- {plant}; Rarity: {info["rarity"]}; Rating: {avg_rating}')
