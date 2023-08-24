sequence = [int(num) for num in input().split()]
avg = sum(sequence) / len(sequence)
sequence.sort(reverse=True)
highest = []

for num in sequence:
    if num > avg:
        highest.append(num)
        if len(highest) == 5:
            break
    else:
        break
if highest:
    print(*highest)
else:
    print('No')