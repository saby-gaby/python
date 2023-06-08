def fill_shells(electrons):
    current_n = 1
    filled_shells = []
    while electrons:
        curr_shell_capacity = 2 * pow(current_n, 2)
        if electrons >= curr_shell_capacity:
            electrons -= curr_shell_capacity
            filled_shells.append(curr_shell_capacity)
        else:
            filled_shells.append(electrons)
            electrons = 0

        current_n += 1

    return filled_shells


number_electrons = int(input())
print(fill_shells(number_electrons))