length = int(input()) / 10   # in decimeter
width = int(input()) / 10   # in decimeter
height = int(input()) / 10   # in decimeter
percent = float(input()) / 100

total_volume = length * width * height
water_volume = total_volume * (1 - percent)

print(water_volume)
