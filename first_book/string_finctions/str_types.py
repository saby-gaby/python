s="hello"
print(s.encode(encoding="utf-8"))
print(s.encode(encoding="utf-16"))
print(s.encode(encoding="cp1251"))

str=bytes("hello", "utf-8")
print(str)
print(str[0], str[1], str[2])

print(len("hello"))
print(len(bytes("hello", "utf-8")))

string=bytearray("hello","utf-8")
print(string)
string[0]=50
print(string)