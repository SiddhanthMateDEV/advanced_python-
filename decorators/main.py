import functools

def mulitplication(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result*4
    return wrapper


@mulitplication
def addition(x):
    return x + 5


print(addition(5))
print(addition.__name__)







def greet(name):
    print(fr"Hello, {name}")
