#program using while true loop to print the banking menu
'''total_balance = 0
while True:
    print("Welcome to the Banking System")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your balance is ", total_balance)
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        total_balance += amount
        print(amount, "deposited successfully")
    elif choice == 3:
        amountW = float(input("Enter the amount to withdraw:"))
        if amountW > total_balance:
            print("Insufficient balance")
        elif amountW < 0:
            print("Withdrawal amount cannot be negative")
        else:
            total_balance -= amountW
            print(amountW, "withdrawn successfully")
    elif choice == 4:
        print("Thank you for using the Banking System")
        break
    else:
        print("Invalid choice")'''



#a program usinng while ture annd also continue statement 
num = int (input("Enter a number: "))
for i in range (1, 11):
    if i == 5:
        continue
    print(num*i)

num = int (input("Enter a number: "))
for i in range (1, 11):
    if i % 3 ==0:
        continue
    print(num*i)

    

