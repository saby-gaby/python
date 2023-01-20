groups = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
total_hikers = 0

for _ in range(groups):
    group = int(input())
    total_hikers += group

    if group <= 5:
        p1 += group
    elif group <= 12:
        p2 += group
    elif group <= 25:
        p3 += group
    elif group <= 40:
        p4 += group
    else:
        p5 += group

print(f'{p1 / total_hikers * 100:.2f}%')
print(f'{p2 / total_hikers * 100:.2f}%')
print(f'{p3 / total_hikers * 100:.2f}%')
print(f'{p4 / total_hikers * 100:.2f}%')
print(f'{p5 / total_hikers * 100:.2f}%')
