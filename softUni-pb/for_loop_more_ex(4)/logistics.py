loads = int(input())
bus, truck, train = 0, 0, 0
total_tons = 0
total_price = 0

for _ in range(loads):
    load = int(input())

    if load <= 3:
        bus += load
    elif load <= 11:
        truck += load
    elif load >= 12:
        train += load

    total_price = (200 * bus) + (175 * truck) + (120 * train)
    total_tons = bus + truck + train

average_price = f'{total_price / total_tons:.2f}'

print(average_price)
print(f'{bus / total_tons * 100:.2f}%')
print(f'{truck / total_tons * 100:.2f}%')
print(f'{train / total_tons * 100:.2f}%')
