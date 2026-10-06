#program to find voter eligibility
citizenship = input("Enter Your Citizenship:")
if citizenship == 'Indian':
    age = int(input("Enter your age:"))
    if age >= 18:
        print("You are Eligibile to vote.")
    else:
        print("You are not Eligibile to vote\n","you need to wait",18 - age,"years")
else:
    print("You are not Eligibile to vote\n","you need to be an Indian citizen")