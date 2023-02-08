x=1             #int
y=2.5           #float
name='John'     #str
is_cool=True    #bool

#multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic math
a=x+y

# Casting
x=str(x)
y=int(y)
z=float(y)

# print(type(z), z)

name='Brad'
age=37
# Concatenate
#print('Hello, my name is '+name+' and I am '+str(age)+'.')

# String formatting

# Arguments by position
#print('Hello, my name is {name} and I am {age}.'.format(name=name, age=age))

# F-Strings (3.6+)
#print(f'Hello, my name is {name} and I am {age}.')

# String Methods
s='hello world'
print(s.capitalize())
print(s.swapcase())
print(s.replace('world', 'everyone'))