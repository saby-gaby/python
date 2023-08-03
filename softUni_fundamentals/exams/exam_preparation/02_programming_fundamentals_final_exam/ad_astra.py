import re

text = input()
pattern = r'([|, #])([a-zA-Z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
products = re.findall(pattern, text)
total_calories = 0
for product in products:
    total_calories += int(product[-1])
print(f'You have food to last you for: {int(total_calories / 2000)} days!')
for product in products:
    print(f'Item: {product[1]}, Best before: {product[2]}, Nutrition: {product[3]}')
