Num = int(input("Enter a number:"))
if Num % 3 == 0:
    print("Fizz")
elif Num % 5 == 0:
    print("Buzz")
elif Num % 3 == 0 and Num % 5 == 0:
    print("FizzBuzz")
else:
    print(Num)

