strings_count = int(input())
search_term = input()
strings = []
filtered_strings = []
for _ in range(strings_count):
    curr_str = input()
    strings.append(curr_str)
    if search_term in curr_str:
        filtered_strings.append(curr_str)
print(strings)
print(filtered_strings)
