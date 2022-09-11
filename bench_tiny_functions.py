

def add(x, y):
    return x + y

def a():
    x = 1
    for n in range(100000):
        add(x, n)

def b():
    x = 1
    for n in range(100000):
        x + n

def aa():
    x = 1
    for n in range(100000):
        add(x, n)
        add(n, x)

def bb():
    x = 1
    for n in range(100000):
        x + n
        n + x

if __name__ == '__main__':
    from timeit import timeit
    NLOOPS = 10**3
    
    print(f"call tiny function, loop={NLOOPS}:")
    t0 = timeit("a()", "from __main__ import a", number=NLOOPS)
    print(t0)
    print(f"call inline function, loop={NLOOPS}:")
    t1 = timeit("b()", "from __main__ import b", number=NLOOPS)
    print(f"{t1} ({(t0-t1)/t0*100:.2f}% faster)")

    print(f"call 2x tiny function, loop={NLOOPS}:")
    t0 = timeit("aa()", "from __main__ import aa", number=NLOOPS)
    print(t0)
    print(f"call 2x inline function, loop={NLOOPS}:")
    t1 = timeit("bb()", "from __main__ import bb", number=NLOOPS)
    print(f"{t1} ({(t0-t1)/t0*100:.2f}% faster)\n")
