#Lambda function
'''x=int(input('Enter the value of x:'))
value=lambda x:x*x # there is no need for us to only with the variable as x, it can be any variable.
print(value(x))'''


#Perfect Number
'''def perfectnum (num):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum
num=int(input("Enter a num"))
num1 = perfectnum(num)
if num == num1:
    print(num,'is a perfect num')
else:
    print(num,'Is not a perfect num')'''



#strong number
Num =int(input("Enter a number:"))

    fact = 1
for i in range(1,Num+1):
    fact = fact * i
