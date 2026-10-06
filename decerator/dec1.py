def dec2(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        print("Result=",fun.__name__,"is",result)
        print("exiting the function")
    return wrapper

@dec2
def product(a,b,c):
    return a*b*c
product(2,3,4)
@dec2
def devision(a,b):
    return a//b
devision(10,2)