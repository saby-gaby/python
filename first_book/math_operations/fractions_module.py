from fractions import Fraction

x = Fraction("0.2") - Fraction("0.1") - Fraction("0.1")
print(x)

a = Fraction(6, 4)
b = Fraction(7, 12)
print("a+b: ", a+b)

c = a*b
print("c=a+b: ", c)

print("Chislitel: ", c.numerator)
print("Znamenatel: ", c.denominator)

print("Convert to float: ", float(c))

print("limit denominator: ", c.limit_denominator(8))

x = 5.75
y = Fraction(*x.as_integer_ratio())
print("from float to fraction: ", y)
