dog_food = int(input()) * 1000

food_eaten = 0

while True:
    eaten = input()

    if eaten == 'Adopted':
        break

    food_eaten += int(eaten)

if dog_food >= food_eaten:
    print(f'Food is enough! Leftovers: {dog_food - food_eaten} grams.')
else:
    print(f'Food is not enough. You need {food_eaten - dog_food} grams more.')
