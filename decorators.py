def decorator(orginal_func):
    print('In The decoratore Function\n')

    def wrapper(*args,**kwargs):
        print(f'wrapper executed before {orginal_func.__name__}()')


        if 1<2:
            print('Yes it is True!!')

            return orginal_func(*args,**kwargs)

    return wrapper

@decorator
def something(x=None,y=None,z='Zahan'):
    print(f'Print something is running now!\n {x} and {y}  {z}')

something(1,7)

# f= decorator(something)()

