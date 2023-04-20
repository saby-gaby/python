record = float(input())
distance = float(input())
seconds_per_meter = float(input())

georg_time = distance * seconds_per_meter + (distance // 50) * 30

if georg_time < record:
    print(f'Yes! The new record is {georg_time:.2f} seconds.')
else:
    print(f'No! He was {georg_time - record:.2f} seconds slower.')
