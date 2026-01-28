def log(func):
    def inner(*args, **kwargs):
        print(f"Called function {func.__name__} with args: {args}, with kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f'Result is: {result}')
        return result
    return inner

@log
def add(x, y):
    return x + y

add(2, 3)

@log
def greet(name, age=20):
    return f"Hello {name}, you are {age}"

greet("Alice", age=25)

def cache(func):
    cash_dict = {}
    def inner(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cash_dict:
            return cash_dict[key]
        result = func(*args, **kwargs)
        cash_dict[key] = result
        return result
    return inner

@cache
def add(x, y):
    print("Calculating...")
    return x + y

print(add(2, 3))
print(add(2, 3))

def authenticate(func):
    def inner(user, *args, **kwargs):
        if user['role'] != 'admin':
            print ('Access denied')
        return func(user, *args, **kwargs)
    return inner
 

@authenticate
def delete_user(user, user_id):
    return f"User {user_id} deleted"

admin_user = {"role": "admin"}
print(delete_user(admin_user, 5))
# User 5 deleted

normal_user = {"role": "user"}
print(delete_user(normal_user, 5))
# Access denied