"""
Create decorator logger. The decorator should print to the console information about function's name and all its arguments separated with ',' for the function decorated with logger.

Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function. 

For example

print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23

print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2

print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two...
onetwo
"""

def logger(func):
    def wrapper(*args, **kwargs):
        all_args = ", ".join(map(str, args + tuple(kwargs.values())))
        result = func(*args, **kwargs)
        print(f"Executing of function {func.__name__} with arguments {all_args}...")
        return result
    return wrapper

@logger
def concat(*args, **kwargs):
    args_str = kwargs_str = ""
    if args: args_str = "".join([f"{sub}" for sub in args])
    if kwargs: kwargs_str = "".join([f"{sub}" for sub in kwargs.values()])
    sum_str = args_str + kwargs_str
    return sum_str

print(concat(1, 2, 3))
print(concat("a", "b", "c"))
print(concat (first = 'one', second = 'two'))
print(concat('first string', second = 2, third = 'second string'))
print(concat(2))