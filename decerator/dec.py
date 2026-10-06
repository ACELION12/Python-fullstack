def dec1(fun):
    def wrapper():
        print('started executing a function')
        print(fun())
        print('finished executing a function')
    return wrapper
@dec1
def greet():
    return 'hello world'
greet()


