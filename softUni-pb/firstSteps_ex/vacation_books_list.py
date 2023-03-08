book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_needed = book_pages / pages_per_hour
daily_pages = hours_needed / days

print(int(daily_pages))
