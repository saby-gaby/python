numbers_count = int(input())
positives = []
negatives = []
for _ in range(numbers_count):
    curr_num = int(input())
    if curr_num >=0:
        positives.append(curr_num)
    else:
        negatives.append(curr_num)
print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}\nSum of negatives: {sum(negatives)}')
