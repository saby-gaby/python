mackerel_price = float(input())  # skumriq cena
sprat_price = float(input())     # caca cena
pan_fish_quantity = float(input())  # palamud k-vo
saffron_quantity = float(input())   # safrid k-vo
mussels_quantity = float(input())   # midi k-vo

pan_fish_price = mackerel_price * 1.6
saffron_price = sprat_price * 1.8
mussels_price = 7.50

to_pay = round(pan_fish_price * pan_fish_quantity + \
    saffron_price * saffron_quantity + \
    mussels_price * mussels_quantity, 2)

print(format(to_pay, '.2f'))
