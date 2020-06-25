from functools import reduce

# HANDS-ON NUMBER 0
'''
a.) Create a list of prime numbers between 0 and 100
b.) Find the sum of all of those prime numbers
c.) Find the digit sum of all of the prime numbers from a.) Hint: use map function
d.) Create a big string from all of the prime numbers from a.)
'''

prime = [x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))]
print(f"All prime numbers: \n{prime}")

print(f"\nSum of all prime numbers: {reduce((lambda x,y: x + y), prime)}")


def digit_sum(s):    # Input is 2 or 1 digit int
    if len(str(s)) < 2:
        return s
    stringed = str(s)
    sum = int(stringed[0]) + int(stringed[1])
    if len(str(sum)) > 1:
        return digit_sum(sum)
    else:
        return sum


print(f"Digit sum of the prime list:\n{list(map(digit_sum, prime))}")

print("\nThe big string of the prime list:")
print("".join([str(x) for x in prime]))