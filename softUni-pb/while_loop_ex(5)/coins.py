coins = 0
change = round(float(input()) * 100)

while change > 0:
    if change >= 200:    # 2 lv - coin
        change -= 200
    elif change >= 100:
        change -= 100
    elif change >= 50:
        change -= 50
    elif change >= 20:
        change -= 20
    elif change >= 10:
        change -= 10
    elif change >= 5:
        change -= 5
    elif change >= 2:
        change -= 2
    elif change >= 1:
        change -= 1

    coins += 1
print(coins)

# without while
# if change // 200 != 0:    # 2 lv - coin
#     coins += change // 200
#     change %= 200
# if change // 100 != 0:
#     coins += change // 100
#     change %= 100
# if change // 50 != 0:
#     coins += change // 50
#     change %= 50
# if change // 20 != 0:
#     coins += change // 20
#     change %= 20
# if change // 10 != 0:
#     coins += change // 10
#     change %= 10
# if change // 5 != 0:
#     coins += change // 5
#     change %= 5
# if change // 2 != 0:
#     coins += change // 2
#     change %= 2
# if change // 1 != 0:
#     coins += change // 1
#     change %= 1
# if change == 0:
#     print(coins)
