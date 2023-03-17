import math

record = float(input())
distance = float(input())
time_meter = float(input())

delay = math.floor(distance / 15) * 12.5
total_time_needed = distance * time_meter + delay

difference = abs(record - total_time_needed)

if total_time_needed < record:
    print(f'Yes, he succeeded! The new world record is {total_time_needed:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
