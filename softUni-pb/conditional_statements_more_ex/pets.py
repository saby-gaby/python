from math import floor, ceil

days = int(input())
food_kg = int(input())
dog_food_one_day = float(input())
cat_food_one_day = float(input())
turtle_food_one_day = float(input()) / 1000

dog_food_needed = days * dog_food_one_day
cat_food_needed = days * cat_food_one_day
turtle_food_needed = days * turtle_food_one_day

total_food_needed = dog_food_needed + cat_food_needed + turtle_food_needed

if total_food_needed <= food_kg:
    print(f'{floor(food_kg - total_food_needed)} kilos of food left.')
else:
    print(f'{ceil(total_food_needed - food_kg)} more kilos of food are needed.')
