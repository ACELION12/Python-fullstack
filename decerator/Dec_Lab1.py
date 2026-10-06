def dec1(fun):
    def wrapper():
        for i in range (1,4):
            print ("Count =",i)
            print(fun())
    return wrapper
@dec1
def word():
    return"hello word"
word()