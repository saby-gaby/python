def increase_decrease(integer):
    if integer <= element:
        integer += element
    elif integer > element:
        integer -= element
    return integer


pokemons = list(map(int,input().split()))
sum_pokemons = 0

while pokemons:
    index = int(input())
    if index < 0:
        element = pokemons[0]
        pokemons[0] = pokemons[-1]
    elif index > len(pokemons) - 1:
        element = pokemons[-1]
        pokemons[-1] = pokemons[0]
    else:
        element = pokemons[index]
        pokemons.pop(index)
    pokemons = list(map(increase_decrease, pokemons))

    sum_pokemons += element

print(sum_pokemons)
