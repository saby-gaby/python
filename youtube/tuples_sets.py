# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Creste tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)
#print(fruits2, type(fruits2))

# Get value 
#print(fruits[1]) # -> Oranges

# Can't change value
#fruits[0]='Pears'  # does not work, because unchangeable

# Delete tuple
del fruits2
#print(fruits2)  # no fruits2

# Get length
#print(len(fruits))

# -------------------------------------------------

# A set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Grapes'}
#print(fruits_set)

# Check if in set
#print('Apples' in fruits_set)  # ->true

# Add to set 
fruits_set.add('Grape')
#print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
#print(fruits_set)

# Add duplicate
fruits_set.add('Apples')
#print(fruits_set)

# Clear set
fruits_set.clear()
#print(fruits_set)

# Delete set
del fruits_set
print(fruits_set)
