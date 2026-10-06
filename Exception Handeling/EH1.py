num=int(input("Enter a number"))
try:
    result=100/num
    print(result)
except Exception as E:
    print(E)
else:
    print("End of pgm")
finally:
    print("Thank You")
