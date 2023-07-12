text = input()
encrypted_text = ""

for char in text:
    new_char_code = ord(char) + 3
    encrypted_text += chr(new_char_code)

print(encrypted_text)

"""
tests: 
Programming is cool! -> Surjudpplqj#lv#frro$
One year has 365 days. -> Rqh#|hdu#kdv#698#gd|v1
"""