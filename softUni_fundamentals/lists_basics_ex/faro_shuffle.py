all_cards = input().split()
shuffles = int(input())
split_on = len(all_cards) // 2
for _ in range(shuffles):
    result_cards = []
    first_half = all_cards[:split_on]
    second_half = all_cards[split_on:]
    for i in range(len(first_half)):
        result_cards.append(first_half[i])
        result_cards.append(second_half[i])
    all_cards = result_cards
print(all_cards)
