# what are pthon decorators
# decorators are functions that modify behaviors of other functions and are usually
# implemented for logging, access control and caching

# 1 how to implement a decorator

import gc


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'before calling {func.__name__}')
        result = func(*args, **kwargs)
        print(f'after calling {func.__name__}')
        return result
    return wrapper


@decorator
def greet(name):
    print(f'hello {name}')

# 2. Explain Python generators and the yield keyword.
# Answer:
# Generators are iterators that lazily produce values one at a time, using yield instead of return.
# They are memory-efficient for large datasets.


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


# 3. How does Python manage memory?
# Python manages memory by using reference counting and garbage collection
a = [1, 2, 3, 4]
b = a
del a
gc.collect()

# 4. What are Python’s *args and **kwargs?
# *args collects positional arguments as a tuple
# **kwargs collects keyword arguments as a dict


def func(*args, **kwargs):
    print('positinal', args)
    print('keyword', kwargs)


if __name__ == '__main__':
   # greet('Alisha')

    for num in fibonacci(5):
        print(num)

    func(1, 2, y=5, z=10)
