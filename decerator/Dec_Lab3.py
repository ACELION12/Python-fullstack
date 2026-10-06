def dec3(fun):
    def wrapper(*args, **kwargs):
        for i in args:
            if i > 0 :
                print(fun(i))
            elif i == 0:
                print(fun(i))
            else:
                print("Invalid: Negative number")
    return wrapper
@dec3
def cal(fun):
    return fun, "The number is Positive and the Square Root is", fun ** 0.5
cal(4, 9, 16, 25, 36,90, 0, -5, -10)