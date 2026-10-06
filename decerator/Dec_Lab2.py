def dec2(fun):
    def wrapper():
        list1 = []

        while True:
            Number = int(input("Enter a number (or enter 0 to finish): "))

            if Number == 0:
                break

            list1.append(Number)

        for Number in list1:

            if Number >= 0:
                print(fun(Number))
            else:
                print("Invalid: Negative number")

    return wrapper


@dec2
def cal(Number):
    return "The number is Positive " \
    "and " \
    "the Square Root is", Number ** 0.5


cal()