# HANDS ON-1
'''
Print the number of unique case-sensitive characters in a string.
String: AppLe
Unique characters: 4

String: aPple
Unique chars: 5

String: aaa
Unique chars: 1
'''

from collections import defaultdict

sample = "aPple"


def unique_chars(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return len(s)


print(unique_chars(sample))
