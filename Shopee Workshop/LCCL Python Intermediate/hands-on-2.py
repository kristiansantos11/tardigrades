# Hands on -2

# Take an input string and report groups of words that start with the same letter.

def report(s):
    d = dict()
    s = s.lower().split()
    for word in s:
        key = word[0].upper()
        d[key] = d.get(key, set() | {word})
    return d


input_string = report('''
        Someday I'll wish upon a star
        Wake up where the clouds are far behind me
        Where trouble melts like lemon drops
        High above the chimney top
        That's where you'll find me
''')

