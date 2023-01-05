input_count = int(input())
p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for _ in range(input_count):
    num = int(input())

    if num < 200:
        p1 += 1
    elif num < 400:
        p2 += 1
    elif num < 600:
        p3 += 1
    elif num < 800:
        p4 += 1
    else:
        p5 += 1

p1 = p1 / input_count * 100
p2 = p2 / input_count * 100
p3 = p3 / input_count * 100
p4 = p4 / input_count * 100
p5 = p5 / input_count * 100

print(f'{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%')
