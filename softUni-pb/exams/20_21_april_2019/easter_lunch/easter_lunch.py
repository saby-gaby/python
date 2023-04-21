easter_bread = int(input())
dozens_eggs = int(input())
cookies = int(input())

easter_bread_price = 3.2
dozen_eggs_price = 4.35
cookies_price = 5.4
egg_paint_price = 0.15

colored_eggs_costs = dozens_eggs * dozen_eggs_price + dozens_eggs * 12 * 0.15

total_costs = easter_bread * easter_bread_price + colored_eggs_costs + cookies * cookies_price

print(format(total_costs, '.2f'))
