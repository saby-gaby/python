walk_minutes = int(input())
count_walks = int(input())
calories_taken = int(input())

calories_burned = count_walks * walk_minutes * 5

if calories_burned >= calories_taken / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.')
