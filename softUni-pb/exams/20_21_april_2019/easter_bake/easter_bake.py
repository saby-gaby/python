from math import ceil

breads = int(input())

total_sugar, total_flour, max_sugar, max_flour = 0, 0, 0, 0

for bread in range(breads):
    sugar = int(input())
    flour = int(input())

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

    total_sugar += sugar
    total_flour += flour

print(f'Sugar: {ceil(total_sugar / 950)}')
print(f'Flour: {ceil(total_flour / 750)}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
