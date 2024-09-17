import functools
import time


def print_timestamp(func):
    @functools.wraps(func)
    def wrapper(*args):
        print('starting time', time.asctime(), 'for number', args[0])  # done before addition
        result = func(*args)   # calls the addition function
        ...                    # actions after addition
        return result
    return wrapper

@print_timestamp
def fibonacci(n):
    """Recursively calculates fibonacci numbers"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# check docstring - would not work without @wraps
print(fibonacci.__doc__)

print(fibonacci(5))
