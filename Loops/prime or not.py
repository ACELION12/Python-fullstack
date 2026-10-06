#code to check the given number is prime or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num // 2 + 1):  # we have taken plus 1 because range does not include the last number and we will only check till half of the number because a number cannot be divisible by any number greater than its half except itself.
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
    