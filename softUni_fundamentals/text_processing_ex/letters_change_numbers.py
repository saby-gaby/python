cards = input().split()
result = 0

for card in cards:
    curr_res = int(card[1:-1])

    if card[0].isupper():
        curr_res /= ord(card[0]) - 64
    else:
        curr_res *= ord(card[0]) - 96
    if card[-1].isupper():
        curr_res -= ord(card[-1]) - 64
    else:
        curr_res += ord(card[-1]) - 96

    result += curr_res

print(f'{result:.2f}')

"""
tests:
A12b s17G -> 330.00
P34562Z q2576f   H456z -> 46015.12
a1A -> 0.00
"""