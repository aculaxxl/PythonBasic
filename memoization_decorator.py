def cache(func):
    cache_dict = {}
    def inner(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        print(key)
        if key in cache_dict:
            return cache_dict[key]

        result = func(*args, **kwargs)
        cache_dict[key] = result
        print(cache_dict)
        return result
    return inner
    print(cache_dict)

@cache
def slow_function(x, y):
    print("Computing...")
    return x / y

print(slow_function(2, 3))
print(slow_function(3, 2))
print(slow_function(2, 3))
print(slow_function(3, 4))