import math

template= """<html>
<head>
<title>%(title)s</title>
</head>
<body>
%(text)s
</body>
</html>"""

data={"title":"My Site", "text": "Content"}

print(template % data)

s="Hello"
print(s.center(20))
print(s.center(20, "*"))
print(s.ljust(20))
print(s.rjust(20))
print(s.ljust(20, "-"))
print(s.rjust(20, "-"))

print("{0}/{1}/{2}".format(30,10,2010))
print("{firstname} {lastname}".format(firstname="John", lastname="Doe"))
print("{lastname}, {0}".format("John", lastname="Doe"))

print("'{0:<15}' '{1:>15}'".format('Hello', 'Hello'))
print("'{0:*<15}' '{1:&>15}'".format('Hello', 'Hello'))

print("'{0:G}' '{1:e}'".format(math.pi,math.pi))
