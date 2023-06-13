def check_happiness(happiness_list, factor):
    happy_or_not = ''
    current_happiness = list(map(lambda x: x * factor, happiness_list))
    total_employees = len(current_happiness)
    average_happiness = sum(current_happiness) / total_employees
    happy_employees = list(filter(lambda x: x >= average_happiness, current_happiness))
    happy_count = len(happy_employees)
    if happy_count < total_employees / 2:
        happy_or_not = 'not '
    return f'Score: {happy_count}/{total_employees}. Employees are {happy_or_not}happy!'


employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())
print(check_happiness(employees_happiness, improvement_factor))