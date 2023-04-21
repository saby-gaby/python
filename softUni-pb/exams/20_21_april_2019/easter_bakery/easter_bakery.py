flour_price = float(input())
flour_weight = float(input())
sugar_weight = float(input())
eggs_packs = int(input())
yeast_packs = int(input())

sugar_price = flour_price * 0.75
egg_packs_price = flour_price * 1.1
yeast_packs_price = sugar_price * 0.2

costs = flour_weight * flour_price + sugar_weight * sugar_price + eggs_packs * egg_packs_price + yeast_packs * yeast_packs_price

print(format(costs, '.2f'))
