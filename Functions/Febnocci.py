#Febnoci number series
'''def febnoci(n):
    n1,n2 = 0,1
    for i in range(n):
        print(n1, end=' ')#0 1 1 2 3 
        n1,n2 = n2,n1+n2
num = int(input("Enter a number:"))
febnoci(num)'''

def msg (name,age):
    if isinstance(name,str) and isinstance(age,int):
        print("Hello",name,'with age:',age)
    else:
        print(isinstance('name',str)) 
        print(isinstance('age',int))       
msg('sathwik',21)