def gen_nums(n):
   # count=1
    '''while count<5:
        yield count
        count+=1
gen1=gen_nums()
for i in gen1:
   print(i)'''
    for i in range(1,n+1):
     yield i
gen1=gen_nums(5)
for i in gen1:
   print(i)
   