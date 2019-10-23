def fib_gen(n):
    a,b=0,1
    while a<n:
        yield a
        a,b = b,a+b


fs = fib_gen(5)
fs.__next__()
fs.__next__()
fs.__next__()
fs.__next__()
fs.__next__()

for i in fib_gen(5):
    print(i)
