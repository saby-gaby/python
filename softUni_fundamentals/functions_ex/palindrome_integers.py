def check_if_palindrome(string):
        if string == string[::-1]:
            return True
        return False


str_list = input().split(", ")
for number in str_list:
    print((check_if_palindrome(number)))
