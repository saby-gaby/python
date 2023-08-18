number_of_heroes = int(input())
hero_book = {}

for _ in range(number_of_heroes):
    hero_details = input().split()
    hero_name, hit_points, mana_points = hero_details[0], int(hero_details[1]), int(hero_details[2])
    if hit_points > 100:
        hit_points = 100
    if mana_points > 200:
        mana_points = 200
    hero_book[hero_name] = {'HP': hit_points, 'MP': mana_points}

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    curr_command, name = command[0], command[1]
    if curr_command == 'CastSpell':
        m_p, spell_name = int(command[2]), command[3]
        if hero_book[name]['MP'] >= m_p:
            hero_book[name]['MP'] -= m_p
            # hero_book[name]['spell'] = spell_name
            print(f'{name} has successfully cast {spell_name} and now has {hero_book[name]["MP"]} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell_name}!')
    elif curr_command == 'TakeDamage':
        damage, attacker = int(command[2]), command[3]
        if damage < hero_book[name]['HP']:
            hero_book[name]['HP'] -= damage
            print(f'{name} was hit for {damage} HP by {attacker} and now has {hero_book[name]["HP"]} HP left!')
        else:
            del hero_book[name]
            print(f'{name} has been killed by {attacker}!')
    elif curr_command == 'Recharge':
        amount = int(command[2])
        if 200 - hero_book[name]['MP'] < amount:
            amount = 200 - hero_book[name]['MP']
        hero_book[name]['MP'] += amount
        print(f'{name} recharged for {amount} MP!')
    elif curr_command == 'Heal':
        amount = int(command[2])
        if 100 - hero_book[name]['HP'] < amount:
            amount = 100 - hero_book[name]['HP']
        hero_book[name]['HP'] += amount
        print(f'{name} healed for {amount} HP!')

for hero, details in hero_book.items():
    print(hero)
    for points, amount in details.items():
        print(f'  {points}: {amount}')
