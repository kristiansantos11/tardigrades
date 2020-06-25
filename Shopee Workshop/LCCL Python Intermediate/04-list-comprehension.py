# Print all the cities inside the city
cities = ['london', 'new delhi', 'ho chi minh']
c = []
for city in cities:
    c.append(city.title())
print(c)

# List comprehension of above code
print([city.title() for city in cities])

# Example 2: names that start with 'h'
c = []
for city in cities:
    if city.startswith('h'):
        c.append(city)
print(c)

# List comprehension of above code
print([city for city in cities if city.startswith('h')])


# Example 3: Nested comprehension
cities = ['helsinski', 'manila', 'tokyo']
c = [(char, i) for city in cities for i, char in enumerate(city) if char in 'aeiou']
print(c)