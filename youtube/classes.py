# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in Python is an object.

# Create class
class User:
    # Constrictor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age +=1

# Extend class
class Customer(User):
    # Constrictor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_ballance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init user object
brad = User("Brad Wuhu", 'test@test.com', 28)
# Init customer
janet = Customer('Janet Johnson', 'test@hey.com', 25)
janet.set_ballance(500)
print(janet.greeting())

#print(type(brad))
#print(brad.age)
#print(brad.greeting())

brad.has_birthday()
#print(brad.age)
