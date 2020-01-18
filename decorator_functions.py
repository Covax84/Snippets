# 1) example of decorator function for original function with no arguments:
def decorator_function_when_no_args(original_function):
    def wrapper_function():
        print('wrapper function executed this before "{}"'.format(original_function.__name__))
        return original_function()
    return wrapper_function  # wrapper is waiting to call(we have no call brackets here)


# one way to use decorators:
def display():
    print('display function executed as variable')


example = decorator_function_when_no_args(display)  # now example is variable waiting to call to execute wrapper function
example()   # wrapper function executed here


# and another way to do the same:
@decorator_function_when_no_args  # this syntax is equal to: display = decorator_function(display); display()
def display():
    print('display function executed with @decorator')


display()  # every time we call display function it is executed with decorator - wrapper


# 2) example of decorator function for original function with arguments:
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper function executed this before "{}"'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display_with_args(name: str, age: int):
    print('display function executed with arguments: Name is {}, age is {}'.format(name, age))


display_with_args('Covax', 35)


# 3) example of decorator class:
class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before "{}"'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_with_args(name: str, age: int):
    print('display function executed with arguments: Name is {}, age is {}'.format(name, age))


@DecoratorClass
def display():
    print('display function with no args executed with @DecoratorClass')


display_with_args('Covax84', 35)
display()
