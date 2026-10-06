#febnocci series
def febno(limit):
    n1,n2=0,1
   # while n1<limit:
    for _ in range(10):
        yield n1
        n1,n2=n2,n1+n2
feb_gen=febno(10)
for i in feb_gen:
    print(i)