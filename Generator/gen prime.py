def primes_gen(limit):
    for n in range(2,limit):
        for i in range(2,n//2+1):
            if n%i==0:
             break
        else:
            yield n
primes=primes_gen(13)
for i in primes:
    print(i)