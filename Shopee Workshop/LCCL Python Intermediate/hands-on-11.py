# Hands on 11
# Create a function that behaves this way

d = {
    ('run', '_'): '_',
    ('run', '|'): '/',
    ('jump', '_'): 'x',
    ('jump', '|'): '|'
}


def foo(act, s):
    print(list(enumerate(act)))
    return ''.join([d[(a, s[i])] for i, a in enumerate(act)])


print(foo(['jump', 'run', 'jump', 'run'], "||__"))
