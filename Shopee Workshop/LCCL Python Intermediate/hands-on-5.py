# Write a function, multsum that takes a number, n. It outputs the sum of multiples
# of 3 and 5 from 0 up to but not including n.


def multsum(x):
    return sum(set(range(3, x, 3)) | set(range(5, x, 5)))

# My own code... It's heavier lol
'''
def multsum(x):
    result = 0
    for n in range(1, x):
        if n % 3 == 0:
            result += n
            continue
        elif n % 5 == 0:
            result += n
            continue
    return result
'''

print(multsum(100))
