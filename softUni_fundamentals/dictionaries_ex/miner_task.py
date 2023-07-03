resources = {}
while True:
    string = input()
    if string == 'stop':
        break
    resource = string
    quantity = int(input())
    if resource in resources:
        resources[resource] += quantity
    else:
        resources[resource] = quantity
for resource, qty in resources.items():
    print(f'{resource} -> {qty}')
