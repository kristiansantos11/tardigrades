# Hands on 6
# Write a function, repeats, that take a string. It outputs the number of characters
# that occur more than once in that string. Ignore casing.

def repeats(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

print(repeats('aaaa'))
print(repeats('abcba'))
