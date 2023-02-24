import random  # or: from random import *

print(random.random(), " => random number")
print(random.uniform(1,100), " => uniform -> random float in range 1-100")
print(random.randrange(1,100,1), " => randrange -> integer in range 1-100")

seq=[8,7,6,5,4,3,2,1]
print(random.choice(seq), "=> random element from seq")
print(random.sample(seq,3), " => sample from seq")
random.shuffle(seq)
print(seq, " => after shuffle")

print(random.randint(1, 20), " => random int in range 1-20")