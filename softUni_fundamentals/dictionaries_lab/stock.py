foods_list = input().split()
foods = {}

for i in range(0, len(foods_list), 2):
    foods[foods_list[i]] = int(foods_list[i + 1])

searches_products = input().split()

for product in searches_products:
    if product in foods:
        print(f'We have {foods[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')
