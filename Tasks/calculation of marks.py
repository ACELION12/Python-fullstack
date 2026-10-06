# read 5 sub marks and if passed in all 5 calculate the percentage and grade and if failed in any subject print fail.
Sub1 = int(input("Enter marks of sub1:"))
Sub2 = int(input("Enter marks of sub2:"))
Sub3 = int(input("Enter marks of sub3:"))
Sub4 = int(input("Enter marks of sub4:"))
Sub5 = int(input("Enter marks of sub5:"))
if Sub1 >= 35 and Sub2 >= 35 and Sub3 >= 35 and Sub4 >= 35 and Sub5 >= 35:
    total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
    percentage = (total/5) 
    print("Total marks is:",total)
    print("Percentage is:",percentage,"%")
    print("Grade is:",end=' ')
    if percentage >= 90:
        print("Grade is: A")
    elif percentage >= 80:
        print("Grade is: B")
    elif percentage >= 70:
        print("Grade is: C")
    elif percentage >= 60:  
        print("Grade is: D")
    elif percentage >= 35:
        print("Grade is: E")
else:
    print("Fail")