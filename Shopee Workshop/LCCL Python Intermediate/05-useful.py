# TERNARY OPERATIONS

# MANUAL VERSION (no ternary operations)
status = ''
n = 10
if n % 2:
    status = 'odd'
else:
    status = 'even'
print(status)

# Shortened:
status = 'odd' if n % 2 else 'even'
print(status)


# ZIP FUNCTION
a = [2, 3, 4]
b = [5, 5, 5]
c = [7, 8, 9, 10]
d = ['a', 'b', 'c']
print(list(zip(a, b, c, d)))
print(dict(zip(d, c)))    # Transform into zipped key-value pairs
print(dict(zip(d, [a, b, c])))    # Transform into zipped key-value(list) pairs


# Filter
n = [11, 12, 33, 43, 55, 66, 76, 80]

def odd(x):
    return x % 2


print(list(filter(odd, n)))


# Map Function - applies a function to an element inside the list
def remainder(x):
    return x % 10


print(list(map(remainder, n)))


# Reduce function
from functools import reduce


def mult(a, b):
    return a * b


print(reduce(mult, n))


# String joins
s = ['a', 'bcd', 'efg', 'hij']
print(" -> ".join(s))

# string translation
sample = "hello world!"
#print(sample.replace('l', 'a'))
t = {'l': '8', 'o': '7'}
table = sample.maketrans(t)    # Creates a translation table
print(sample.translate(table))

# Another way:
sample2 = "hello world!"
#print(sample.replace('l', 'a'))
s1 = 'l8'
s2 = 'o7'
table = sample2.maketrans(s1, s2, '!')    # Creates a translation table
print(sample2.translate(table))

