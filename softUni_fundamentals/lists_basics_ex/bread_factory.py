initial_energy = 100
coins = 100
day_events = input().split('|')
current_energy = initial_energy
is_closed = False
for event in day_events:
    event, value = event.split('-')
    value = int(value)
    if event == 'rest':
        if current_energy + value > initial_energy:
            print(f'You gained {initial_energy - current_energy} energy.')
            current_energy = 100
        else:
            current_energy += value
            print(f'You gained {value} energy.')
        print(f'Current energy: {current_energy}.')
    elif event == 'order':
        if current_energy >= 30:
            current_energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
    else:
        ingredient = event
        if coins >= value:
            coins -= value
            print(f'You bought {ingredient}.')
        else:
            is_closed = True
            print(f'Closed! Cannot afford {ingredient}.')
            break
if not is_closed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {current_energy}')

# events = input().split("|")
# total_energy = 100
# total_coins = 100
# factory_is_open = True
# for event in events:
#     event_items = event.split("-")
#     type_of_event = event_items[0]
#     event_value = int(event_items[1])
#     if type_of_event == "rest":
#         current_energy = total_energy
#         total_energy += event_value
#         if total_energy > 100:
#             total_energy = 100
#         gained_energy = total_energy - current_energy
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {total_energy}.")
#     elif type_of_event == "order":
#         if total_energy >= 30: #order can be completed
#             total_energy -= 30
#             total_coins += event_value
#             print(f"You earned {event_value} coins.")
#         else:
#             total_energy += 50
#             print("You had to rest!")
#     else:
#         if total_coins >= event_value:
#             total_coins -= event_value
#             print(f"You bought {type_of_event}.")
#         else:
#             factory_is_open = False
#             break
# if factory_is_open: #if factory is open == True
#     print("Day completed!")
#     print(f"Coins: {total_coins}")
#     print(f"Energy: {total_energy}")
# else:
#     print(f"Closed! Cannot afford {type_of_event}.")
