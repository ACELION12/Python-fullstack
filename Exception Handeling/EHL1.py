'''Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer'''

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    raise ValueError("Input is not a valid integer.")