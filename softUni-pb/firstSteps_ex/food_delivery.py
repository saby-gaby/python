chicken_menus = int(input())
fish_menus = int(input())
vegi_menus = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegi_menu_price = 8.15
delivery_price = 2.50

menus_costs = \
    (chicken_menus * chicken_menu_price) + \
    (fish_menus * fish_menu_price) + \
    (vegi_menus * vegi_menu_price)
dessert_costs = menus_costs * 0.2

total_costs = menus_costs + dessert_costs + delivery_price

print(round(total_costs, 2))
