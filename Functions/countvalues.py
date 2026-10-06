'''⁠ ⁠Write a Python program to Count all letters, digits, and special
symbols from the given string
Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 2 Symbol = 3
'''

Pass = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

for i in Pass:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        digits += 1
    else:
        symbols += 1

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)