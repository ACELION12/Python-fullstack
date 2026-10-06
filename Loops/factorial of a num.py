#factorial of a number.
Num =int(input("Enter a number:"))
fact = 1
for i in range(1,Num+1):
    fact = fact * i
print("Factorial of",Num,"is:",fact)

num = int(input("Enter a num:"))
fact = 1
for i in range (num,0,-1):
    fact = fact * i
    print(fact, end='\n',)
print("Factorial of",num,"is:",fact)


