# what are pthon decorators
# decorators are functions that modify behaviors of other functions and are usually
# implemented for logging, access control and caching

# how to implement a decorator

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


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


if __name__ == '__main__':
   # greet('Alisha')

    for num in fibonacci(5):
        print(num)
