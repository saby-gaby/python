snowballs_count = int(input())
highest_value, top_weight, top_time, top_quality = 0, 0, 0, 0

for snowball in range(snowballs_count):
    weight = int(input())
    time = int(input())
    quality = int(input())
    snowball_value = (weight / time) ** quality

    if snowball_value > highest_value:
        highest_value = int(snowball_value)
        top_weight = weight
        top_time = time
        top_quality = quality
print(f'{top_weight} : {top_time} = {highest_value} ({top_quality})')
