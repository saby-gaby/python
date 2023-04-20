days = int(input())
food = float(input())

total_dog, total_cat, biscuits = 0, 0, 0

for day in range(1, days + 1):
    eaten_by_dog = int(input())
    eaten_by_cat = int(input())

    total_dog += eaten_by_dog
    total_cat += eaten_by_cat

    if day % 3 == 0:
        biscuits += (eaten_by_dog + eaten_by_cat) * 0.1

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{(total_cat + total_dog) / food * 100:.2f}% of the food has been eaten.')
print(f'{total_dog / (total_cat + total_dog) * 100:.2f}% eaten from the dog.')
print(f'{total_cat / (total_cat + total_dog) * 100:.2f}% eaten from the cat.')
