def check_ticket(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'
    left_side = ticket[:10]
    right_side = ticket[10:]
    winning_symbols = ['@', '#', '$', '^']
    for symbol in winning_symbols:
        for count_symbols in range(10, 5, -1):
            match_section = count_symbols * symbol
            if match_section in left_side and match_section in right_side:
                if count_symbols == 10:
                    return f'ticket "{ticket}" - {count_symbols}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {count_symbols}{symbol}'
    return f'ticket "{ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(', ')]

for curr_ticket in tickets:
    print(check_ticket(curr_ticket))

"""
tests:
Cash$$$$$$Ca$$$$$$sh -> ticket "Cash$$$$$$Ca$$$$$$sh" - 6$
$$$$$$$$$$$$$$$$$$$$, aabb   , th@@@@@@eemo@@@@@@ey -> ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!\ninvalid ticket\nticket "th@@@@@@eemo@@@@@@ey" - 6@
validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$ -> ticket "validticketnomatch:(" - no match\nticket "Cas$$$$$$$Ca$$$$$$s$" - 6$
"""
