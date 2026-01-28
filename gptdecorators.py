def simple_decorator(func):
    def inne():
        print("Function is called")
        func()
    return inne



@simple_decorator
def my_func():
    print("Hello")

my_func()

def count_calls(func):
    count = 0
    def inner():
        nonlocal count 
        count += 1
        print(f"Call #{count}")
        func()
    return inner

@count_calls
def my_func():
    print("Hello")

my_func()
my_func()
my_func()

def repeat(calls):
    def decorator(func):
        def inner(): 
            for _ in range(calls):
                func()
        return inner
    return decorator
    
@repeat(5)
def my_func():
    print("Five hello")

my_func()
