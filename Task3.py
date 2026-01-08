def decorator(*args,**kwargs):
    def second_decorator(func):
        def wrapper(*args2, **kwargs2):
           print('names of variables are ', kwargs['variable_names'])
           func(*args2, **kwargs2)
           print('Function is finished')
        return wrapper
    return second_decorator

@decorator(variable_names= "a and b")
def fun(a,b):
    return print(a+b)

fun(3,4)