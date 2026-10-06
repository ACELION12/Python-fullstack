'''Atoy vendor supplies three types of toys: Battery Based Toys, Key-based
Toys, and Electrical Charging Based Toys. The vendor gives a discount of
10% on orders for battery-based toys if the order is for more than Rs. 1000.
On orders of more than Rs. 100 for key-based toys, a discount of 5% is
given, and a discount of 10% is given on orders for electrical charging based
toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
are used for battery based toys, key-based toys, and electrical charging based
toys respectively. Write a program that reads the product code and the order
amount and prints out the net amount that the customer is required to pay
after the discount'''

code = int(input("1-Battery\n2-Key\n3-Electrical\nEnter the code: "))
if code not in [1, 2, 3]:
    print("Invalid code")
    exit()
    
amount = float(input("Enter order amount: "))

discount = 0 

if code == 1 and amount > 1000:
    discount = amount * 0.10
elif code == 2 and amount > 100:
    discount = amount * 0.05
elif code == 3 and amount > 500:
    discount = amount * 0.10

net_amount = amount - discount 
discount_amount = amount * 0.10 if code == 1 and amount > 1000 else amount * 0.05 if code == 2 and amount > 100 else amount * 0.10 if code == 3 and amount > 500 else 0

print("Discount amount = Rs.", discount_amount)
print("Net amount to be paid = Rs.", net_amount)