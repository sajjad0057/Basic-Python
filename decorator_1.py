"""
In Python, functions are the first class objects, which means that –

   -> Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
   -> Functions can be defined inside another function and can also be passed as argument to another function.
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

"""

# def outer(message):
#     print("In the outer function")
#
#     def inner():
#         print("Calling the inner function")
#         print(message)
#
#     return inner()
# outer("Hello world")

# Every decorators has a rapper function... basically rapper function can modify original_func but not permanant..
def decorator(passed_func):
    print('In the decorator function\n')

    def wrapper():
        print(f'wrapper executed before {passed_func.__name__}()')
        if True:
            print("Yes it is True")
        return passed_func()
    return wrapper


# Using Decorator in one Way :
# def print_something():
#     return print("print_something is being run !")
#
# f = decorator(print_something)
# f()

# using decorator in another way :
@decorator
def print_something():
    return print("print_something is being run !")
print_something()



