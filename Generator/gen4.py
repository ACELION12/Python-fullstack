list1=[1,4,3,9,6,8]
gen2=(i*3 for i in list1 if i%3==0)
for n in gen2:
  print(n)