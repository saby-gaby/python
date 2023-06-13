def find_palindrome(lst, palindrome):
    all_palindrome_found = [word for word in lst if word == word[::-1]]
    palindrome_found = [word for word in lst if word == palindrome]
    count_found = len(palindrome_found) if palindrome in lst else 0

    print(all_palindrome_found)
    print(f'Found palindrome {count_found} times')

words = input().split()
target_palindrome = input()

find_palindrome(words, target_palindrome)
