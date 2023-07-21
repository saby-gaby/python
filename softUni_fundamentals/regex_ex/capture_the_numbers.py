import re

pattern = r'\d+'
line = input()

while line:
    res = re.findall(pattern, line)
    if res:
        print(*res, end=' ')
    line = input()


"""
The300
What is that?
I think it's the 3rd movie
Let's watch it at 22:45 -> 300 3 22 45

123a456
789b987
654c321
0 -> 123 456 789 987 654 321 0
"""

