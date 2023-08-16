import re

number_codes = int(input())
pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

for _ in range(number_codes):
    barcode = input()
    code_info = re.match(pattern, barcode)
    product_group = ''
    if code_info:
        for char in code_info.group(1):
            if char.isdigit():
                product_group += char
        if not product_group:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
