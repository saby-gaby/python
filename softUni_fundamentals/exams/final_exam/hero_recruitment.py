command = input().split()
spellbook = {}

while command[0] != 'End':
    curr_command = command[0]
    hero_name = command[1]
    if curr_command == 'Enroll':
        if hero_name not in spellbook.keys():
            spellbook[hero_name] = []
        else:
            print(f'{hero_name} is already enrolled.')
    elif curr_command == 'Learn':
        spell_name = command[2]
        if hero_name in spellbook.keys():
            if spell_name not in spellbook[hero_name]:
                spellbook[hero_name].append(spell_name)
            else:
                print(f'{hero_name} has already learnt {spell_name}.')
        else:
            print(f'{hero_name} doesn\'t exist.')
    elif curr_command == 'Unlearn':
        spell_name = command[2]
        if hero_name in spellbook.keys():
            if spell_name in spellbook[hero_name]:
                spellbook[hero_name].remove(spell_name)
            else:
                print(f'{hero_name} doesn\'t know {spell_name}.')
        else:
            print(f'{hero_name} doesn\'t exist.')

    command = input().split()

if spellbook:
    print('Heroes:')
    for hero, spells in spellbook.items():
        print(f'== {hero}:', end=" ")
        print(*spells, sep=', ')