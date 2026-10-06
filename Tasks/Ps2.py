#Factorial with recursion

'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


numbers = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

result = {key: factorial(value) for key, value in numbers.items()}

print(result)'''

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))