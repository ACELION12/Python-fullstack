#program to write a pallindrome number
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    rem = num % 10 # Extract the last digit
    rev = (rev * 10) + rem # Build the reversed number
    num = num // 10 # Remove the last digit
if temp == rev:
    print(temp, "is a palindrome number")
else:
    print(temp, "is not a palindrome number")