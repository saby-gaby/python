budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
loaves, colored_eggs = 0, 0

while True:
    if budget >= milk_price + flour_price + eggs_price:
        budget -= milk_price + flour_price + eggs_price
    else:
        break
    loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2
print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
