# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# COMPREHENSION
# ======================
print()

# EXAMPLE 1: capitalize city names

cities = ['helsinki', 'new delhi', 'ho chi minh']
c = [] 
for city in cities:
    c.append(city.title())
print(c)


# EXAMPLE 2: names that start with 'h'
# c = [] 
# for city in cities:
#     if city.startswith('h'):
#         c.append(city)
# print(c)


# EXAMPLE 3: nested comprehensions
# [('e', 1), ('i', 4), ('i', 7), ('e', 1), ('e', 5), ('i', 8), ('o', 1), ('i', 5), ('i', 8)]
# print(c)


# OTHER EXAMPLES
# Set of non-letter characters in the string
numbers = {char for char in 'H3LL* W*RLD' if not char.isalpha()}
# print(numbers)

# Dictionary of key-value pairs where key is a city and value is the number of 'i' in the city name
icount = {city: city.count('i') for city in cities}
# print(icount)

print()