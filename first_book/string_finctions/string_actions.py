s='123'
print(s[0],s[1],s[2], ' => by index')
# print(s[3])  #error: string index out of range 
print(s[-1],s[-2],s[-3], ' => by index revers')

s= 'Hello'
print(s[:], ' => fom pos 1 to the end')
print(s[:-1:], ' => cut the last symbol')
print(s[1::2], ' => start on pos 1 to the end with step 2')
print(s[1::], ' => cut the first symbol')

print("1"+"2" )
print("1" "2" )

s="1","2"
print(s)
print(type(s))

print("hell"in"Hello")
print("hell"in"hello")

print("*" * 20)

s="123456"
print(len(s))

for i in range(len(s)): 
    print(s[i], end=" ")