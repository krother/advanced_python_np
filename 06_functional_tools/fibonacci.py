"""
0 1 1 2 3 5 8 13 21 34 ...
"""
import functools
import time
from typing import Callable


def print_timestamp(func: Callable) -> Callable:
    """the decorator function has a function as its argument (fibonacci())"""
    @functools.wraps(func)
    def wrapper(*args):
        """
        inner function
        1. prints a timestamp
        2. calls fibonacci
        3. returns the result of fibonacci
        """
        print('starting time', time.asctime(), 'for number', args[0])  # done before addition
        result = func(*args)   # calls the addition function
        ...                    # actions after addition
        return result
    return wrapper  # return a function that replaces fibonacci


@print_timestamp
def fibonacci(n):
    """Recursively calculates fibonacci numbers"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@print_timestamp
def add(a, b):
    return a + b


# check docstring - would not work without @wraps
print(fibonacci.__doc__)

#print(fibonacci(5))

print(add(3, 4))
