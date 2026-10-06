#program for leap year using if else condition 
Year = int(input("Enter a Year: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(Year, "is a leap year")
else:
    print (Year,"is not a leap year")
    