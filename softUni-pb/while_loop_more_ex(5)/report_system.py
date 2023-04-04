target_sales = int(input())

cash_total = 0
card_total = 0
transactions_counter = 0
cash_counter = 0
card_counter = 0

while cash_total + card_total < target_sales:
    transaction = input()

    if transaction == 'End':
        print('Failed to collect required money for charity.')
        break

    transaction = int(transaction)
    transactions_counter += 1

    if transactions_counter % 2 != 0:
        if transaction <= 100:
            cash_counter += 1
            print('Product sold!')
            cash_total += transaction
        else:
            print('Error in transaction!')
    else:
        if transaction > 10:
            card_counter += 1
            print('Product sold!')
            card_total += transaction
        else:
            print('Error in transaction!')
else:
    print(f'Average CS: {cash_total / cash_counter:.2f}')
    print(f'Average CC: {card_total / card_counter:.2f}')
