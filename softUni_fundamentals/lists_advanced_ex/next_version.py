def generate_next_version(curr_version):
    curr_version = int(curr_version.replace(".", ""))
    new_version = '.'.join(str(curr_version + 1))
    return new_version

print(generate_next_version(input()))
