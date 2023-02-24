import math

a=float('inf')
b=float('-inf')
c=float('nan')

print(a, " => infinity")
print(b, " => -infinity")
print(c, " => NaN")

print(math.isinf(a), " => is a infinity")
print(math.isinf(b), " => is b infinity")
print(math.isinf(c), " => is c infinity")
print(math.isnan(c), " => is c NaN")