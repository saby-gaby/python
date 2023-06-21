class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            info = f'Mammals in {self.name}: {", ".join(self.mammals)}'
        elif species == 'fish':
            info = f'Fishes in {self.name}: {", ".join(self.fishes)}'
        elif species == 'bird':
            info = f'Birds in {self.name}: {", ".join(self.birds)}'
        info += f'\nTotal animals: {Zoo.__animals}'

        return info

zoo_name = Zoo(input())
animals_count = int(input())

for _ in range(animals_count):
    species, name = input().split()
    zoo_name.add_animal(species, name)

print(zoo_name.get_info(input()))

# 
# print(Zoo.__dict__)