list1=[1,2,3,1,4,6,3]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
for i in list2:
    if list1.count(i)>1:
        print(i)



