#write a program for providing discount on a bill based on given condition.
'''bill is 2000>= 10% discount
1000>=5% discount
<1000 no discount'''
Billamount = int(input("Enter your Bill Amount:"))
if Billamount >= 2000:
    discount1 = Billamount * 10 /100
    print("You are Eligibile for 10% discount\n","Your Discount Amount is:",discount1)
    print("Your Total Bill Amount is:",Billamount - discount1)
elif Billamount >=1000:
    discount2 = Billamount * 5 /100
    print("You are Eligibile for 5% discount\n","Your Discount Amount is:",discount2)
    print("Your Total Bill Amount is:",Billamount - discount2)
else:
    print("No Discount is available\n","Your Total Bill Amount is:",Billamount)