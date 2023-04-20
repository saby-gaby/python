btc = int(input())
juan = float(input())
commission = float(input()) / 100

btc_lv = btc * 1168
juan_usd = juan * 0.15
usd_lv = juan_usd * 1.76
euro = (btc_lv + usd_lv) / 1.95

print(f'{euro - euro * commission:.2f}')
