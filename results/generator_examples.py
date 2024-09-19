"""
Generator Functions

OOP organizes state | Functional programming is stateless

benefit of being stateless: no bugs involving variables
"""

def numbers():
    n = 1
    while True:
        yield n
        n += 1

gen = numbers()
print(next(gen))
print([next(gen) for i in range(10)])

# generator instances are independent
b = gen()
b = numbers()
print([next(b) for i in range(10)])


# generate square numbers
def square():
    n = 1
    while True:
        yield n ** 2
        n += 1

s = square()
print([next(s) for i in range(10)])

# generator expression
sq = (n ** 2 for n in numbers())
print([next(sq) for i in range(10)])

# generator from another generator
s3 = (n ** 2 for n in sq)
print(next(s3))

# you find lots of generators in the itertools module
from itertools import cycle, permutations

c = cycle("ABC")
print([next(c) for i in range(10)])

p = permutations("ABC")
print(list(p))

# when are generators useful?
# - helps to model mathematical series that are infinite
# - discipline to exercise programming
# - reading large files
f = open("../05_test_automation/zen_of_python.txt")
next(f)  # reads one line
