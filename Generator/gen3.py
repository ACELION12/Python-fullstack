def nums(limit):
    for i in range(1,limit):
        yield i**2
gen1=nums(5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))