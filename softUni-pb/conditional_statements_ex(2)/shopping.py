budget = float(input())
vga = int(input())
cpu = int(input())
ram = int(input())

vga_price = vga * 250
cpu_price = cpu * (vga_price * 0.35)
ram_price = ram * (vga_price * 0.1)

total_sum = vga_price + cpu_price + ram_price

if vga > cpu:
    total_sum *= 0.85

diff = f'{abs(budget - total_sum):.2f}'

if budget >= total_sum:
    print(f'You have {diff} leva left!')
else:
    print(f'Not enough money! You need {diff} leva more!')
