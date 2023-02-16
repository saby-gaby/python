# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')
#print(person2, type(person2))

# Get value 
#print(person['first_name'])
#print(person.get('last_name'))

# Add key/value
person['phone']= '555-555-5555'

print(person)

# Get dict keys
#print(person.keys())

# Get dict items
#print(person.items())

# Copy dict
person3=person.copy()
person3['city'] = 'Boston'
#print(person3)

# Remove item
del(person['age'])
person.pop('phone')
#print(person)

# Clear
person.clear()
#print(person)

# Get length
#print(len(person3))

# List of dict
people = [
    {'name':'Marta', 'age': 30},
    {'name':'Kevin', 'age': 25}
]

print(people)
print(people[0]['name'])  # -> Marta