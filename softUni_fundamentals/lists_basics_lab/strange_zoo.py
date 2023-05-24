animal = []
for body_part in range(3):
    body_part = input()
    animal.append(body_part)
animal[0], animal[2] = animal[2], animal[0]
print(animal)
