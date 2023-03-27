type_flowers = input()
count_flowers = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.8
tulips_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5
total_costs = 0

if type_flowers == 'Roses':
    total_costs = count_flowers * roses_price

    if count_flowers > 80:
        total_costs *= 0.9
elif type_flowers == 'Dahlias':
    total_costs = count_flowers * dahlias_price

    if count_flowers > 90:
        total_costs *= 0.85
elif type_flowers == 'Tulips':
    total_costs = count_flowers * tulips_price

    if count_flowers > 80:
        total_costs *= 0.85
elif type_flowers == 'Narcissus':
    total_costs = count_flowers * narcissus_price

    if count_flowers < 120:
        total_costs *= 1.15
elif type_flowers == 'Gladiolus':
    total_costs = count_flowers * gladiolus_price
    
    if count_flowers < 80:
        total_costs *= 1.2

if budget >= total_costs:
    print(f'Hey, you have a great garden with {count_flowers} {type_flowers} and {budget - total_costs:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_costs - budget:.2f} leva more.')
