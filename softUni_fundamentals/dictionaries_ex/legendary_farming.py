materials = {}
collected_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
has_legendary_item = False

while not has_legendary_item:
    incoming_materials = input().lower().split()
    for i in range(1, len(incoming_materials), 2):
        key = incoming_materials[i]
        value = int(incoming_materials[i - 1])
        if key not in collected_materials:
            collected_materials[key] = 0
        collected_materials[key] += value

        if collected_materials['shards'] >= 250:
            collected_materials["shards"] -= 250
            print('Shadowmourne obtained!')
            has_legendary_item = True
            break
        if collected_materials["fragments"] >= 250:
            collected_materials["fragments"] -= 250
            print('Valanyr obtained!')
            has_legendary_item = True
            break
        if collected_materials["motes"] >= 250:
            collected_materials["motes"] -= 250
            print('Dragonwrath obtained!')
            has_legendary_item = True
            break

for material, qty in collected_materials.items():
    print(f'{material}: {qty}')
