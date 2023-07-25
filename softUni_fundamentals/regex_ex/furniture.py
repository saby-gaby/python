import re

purchase = input()
pattern = r'>>(?P<furniture_name>[A-Z]+[a-z]*)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'
costs = 0
print('Bought furniture:')

while purchase != 'Purchase':
    purchased_item = re.match(pattern, purchase)
    if purchased_item:
        item = purchased_item.groupdict()
        print(item['furniture_name'])
        price = float(item['price'])
        qty = int(item['quantity'])
        costs += price * qty

    purchase = input()

print(f'Total money spend: {costs:.2f}')


"""
test:
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase -> Bought furniture:
            Sofa
            TV
            2436.69
"""
