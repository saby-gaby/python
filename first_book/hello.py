print("Hello World!")
# a=2; b=3; c=4; x = a + b * c;
# print(x)

# x=0
# while x < 5:
#    print(x)
#    x+=1
# print("The End!")
#
# for x in range (1,10):print(x)

# try:
#    name = input("What is your name? \n")
#    print("Hello ", name)
# except EOFError:
#    print("EOFError raised")

# x=float(input("Enter x= \n"))
# y=float(input("Enter y= \n"))
# print(x+y)
# input()

# import sys
# args = sys.argv[:]
# for n in args:
#     print(n)
#     print(type(n))


# time to reach the destination
# dist=0
# speed=0
# dist=int(input("Distance to be reached: "))
# speed=int(input("Planned average speed: "))
# time = dist*60/speed
#
# print("Will be spent ",time, " mins.")


# fuel consumption
# consum = 0
# dist = 0
# consum = float(input("Enter average fuel consumption 1/100 km:"))
# dist = float(input("Enter teh distance, km:"))
# result=consum*dist/100
# print("Need ", result, " l.")

# correct data-type
# service = float(input("Enter the cost of maintenance:"))
# fuel = float(input("Cost of fuel:"))
# tax = float(input("Taxes and Duties:"))
# tuning = float(input("Tuning:"))
# insurance = float(input("Cost of insurance:"))
# total = service + fuel + tax + tuning + insurance
# print("Total: ", total)


# print("Hello, " + "World!")


# Kalculator
""" print("*" * 15, "Калкулатор ", "*" * 10)
print("За изход от програмата въведете q в качеството на знак за операция")
while True:
    s=input("Знак (+, -, *, /): ")
    if s=="q": break
    if s in ('+','-', '*', '/'):
        x=float(input("x="))
        y=float(input("y="))
        if s=='+':
            print("%.2f" % (x+y))
        elif s=="-":
            print("%.2f" % (x-y))
        elif s=="*":
            print("%.2f" % (x*y))
        elif s=="/":
            if y!=0:
                print("%.2f" % (x/y))
            else:
                print("Деление на нула!")
    else:
        print("Неверен знак за операция!") """


# if..else
""" n=int(input("Input N: "))
if n < 100: print("n < 100")
else: print(" n > 100") """

# print("""Select your Browser:
# 1 - Google Chrome
# 2 - Firefox
# 3 - MS Internet Explorer
# 4 - Opera
# 5 - Safari
# 6 - Other""")
# browser = int(input(""))
# if browser == 1:
#     print("Chrome")
# elif browser == 2:
#     print("Firefox")
# elif browser == 3:
#     print("MS IE")
# elif browser == 4:
#     print("Opera")
# elif browser == 5:
#     print("Safari")
# elif browser == 6:
#     print("Other")
# else:
#     print("Incorrect input")

""" age=int(input("Your age is: "))
if age < 18:
    print("Съжаляваме, достъпът е ограничен!")
    print("Заповядай отново, когато станеш на 18!") """


# for loop
""" for i in range(1,10):
    print(i)
    if i == 6:
        break
else: print("Done!") """

""" dict = {"g":1, "a":5, "b":2}
for key in sorted(dict.keys()):
    print(key, " => ", dict[key]) """

# for letter in "word": print(letter)


# while loop
n = 0
""" while True:
    print("Hello")
    n+=1
    if n==5: break """
""" while n<10:
    print("Hello")
    n+=1 """

""" for n in range(1,20):
    if n==5:
        print("hu-hu")
        continue
    if n==12:
        break
    print(n) """


""" for i in range(10):
    print(i, end=" ")
    print() """

""" for i in range(0,50,5):
    print(i, end=" ")
    print() """

""" for i in range(10,0,-1):
    print(i, end=" ")
    print() """

# access-level
level = 0
login = ""
while not login:
    login = input("Login: ")
password = ""
while not password:
    password=input("Password: ")
if login=="root" and password=="123":
    level=10
elif login=="den" and password=="321":
    level=5
if level:
    print("Hello, ", login)
    print("Your access level is ", level)
else:
    print("Access denied!")
