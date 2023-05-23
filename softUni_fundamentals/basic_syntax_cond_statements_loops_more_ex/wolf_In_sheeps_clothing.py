queue = input().split(', ')
queue.reverse()
position_counter = 0

for animal in queue:
    if animal == 'wolf' and position_counter == 0:
        print('Please go away and stop eating my sheep')
    elif animal == 'wolf':
        print(f'Oi! Sheep number {position_counter}! You are about to be eaten by a wolf!')
    position_counter += 1
