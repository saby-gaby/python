def sort_by_length(names_list):
    sorted_list = sorted(names_list, key=lambda x: (-len(x), x))
    return sorted_list

print(sort_by_length(input().split(', ')))
    