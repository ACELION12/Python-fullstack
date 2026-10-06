def gen_value():
    yield 1
    yield 2
    yield 3
gen=gen_value()
for i in gen:
    print(i)