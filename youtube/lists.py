# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers=[1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use constructor
numbers2= list((1, 2, 3, 4, 5))
#print(numbers, numbers2)

# Get a value
#print(fruits[1]) #Oranges

# Get lenth
#print(len(fruits))

# Append to a list
fruits.append('Mangos')
#print(fruits)

# Remove from list
fruits.remove("Grapes")
#print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
#print(fruits)

# Change value
fruits[0]= 'Blueberries'
#print(fruits)

# Remove with pop
fruits.pop(2)
#print(fruits)

# Revers list
fruits.reverse()
#print(fruits)

#sort list
fruits.sort()
#print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)

