veg_price = float(input())
fruits_price = float(input())
veg_weight = int(input())
fruits_weight = int(input())

veg_income_lv = veg_weight * veg_price
fruits_income_lv = fruits_weight * fruits_price
total_lv = veg_income_lv + fruits_income_lv
total_euro = format(total_lv / 1.94, '.2f')

print(total_euro)
