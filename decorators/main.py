import functools

def start_end_decorator(func):
    def wrapper(*args,**kwargs):
        print("START")
        result = func(*args,**kwargs)
        print("END")
        return result
    return wrapper


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


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat




@repeat(num_times=3)
def greet(name):
    print(fr"Hello, {name}")


greet('alex')


def debug(func):
    def wrapper(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self,*args,**kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args,**kwargs)
        # print("Hi there")

# cc = CountCalls(None)
# cc()

# @CountCalls
# @debug
# @start_end_decorator
@CountCalls
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello('Alex')
say_hello('Alex')
say_hello('Alex')
say_hello('Alex')
say_hello('Alex')
