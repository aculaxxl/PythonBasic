def log(func):
    def inner(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and with kwargs: {kwargs}")

        result = func(*args, **kwargs)
        print(f'Result is {result}')
        return result
    return inner

@log
def add(x, y):
    return x + y

add(2, 3)

def require_role(role):
    def decorator(func):
        def inner(*args, **kwargs):
            user = kwargs.get("user") or (args[0] if args else None)
            if not user or user.get("role") != role:
                return "Access denied"
            return func(*args, **kwargs)
        return inner
    return decorator
            
user_admin = {"name": "Alice", "role": "admin"}
user_guest = {"name": "Bob", "role": "guest"}

@require_role("admin")
def delete_user(user):
    return "User deleted"

print(delete_user(user_admin))
print(delete_user(user_guest))

def trace(func):
    def inner(*args, **kwargs):
        print(f"Called function {func.__name__}, with args: {args}, kwargs: {kwargs} ")
        result = func(*args, **kwargs)
        print(f"Result is {result}")
        return result
    return inner

@trace
def multiply(x, y):
    return x * y

multiply(2, 3)



def validate_args(func):
    def inner(*args, **kwargs):
        for arg in args:
            if type(arg) != int:
                return "Invalid arguments"
        for value in kwargs.values():
            if type(value) !=str:
                return "Invalid arguments"
        result = func(*args, **kwargs)
        return result
    return inner

                



@validate_args
def process(a, b, name=None):
    return f"{name}: {a + b}"


print(process(2, 3, name="Alice"))      # OK
print(process(2, "3", name="Bob"))      # Invalid arguments
print(process(2, 3, name=123))       