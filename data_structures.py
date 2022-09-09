from collections import namedtuple

STest = namedtuple('TEST', 'a b c')
a = STest(a=1,b=2,c=3)

class Test(object):
    __slots__ = ['a','b','c']
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

b = Test(1,2,3)
c = {'a':1, 'b':2, 'c':3}
d = (1,2,3)
e = [1,2,3]
key = 2

if __name__ == '__main__':
    from timeit import timeit
    nrepeat = 100000

    print("=== Definition ===\n")
    print("Define NamedTuple with a, b, c:")
    print(timeit("""\
STest = namedtuple('TEST', 'a b c')""", """\
from collections import namedtuple""", number=nrepeat))

    print("Define Class with a, b, c slots:")
    print(timeit("""\
class Test(object):
    __slots__ = ['a','b','c']
def __init__(self, a, b, c):
    self.a=a
    self.b=b
    self.c=c""", number=nrepeat))

    print("Define Tuple with 3 values:")
    print(timeit("('a','b','c')", number=nrepeat))

    print("\n=== Instantiation ===\n")

    print("Instantiate NamedTuple with a, b, c:")
    print(timeit("""a = STest(a=1,b=2,c=3)""", """from __main__ import STest""", number=nrepeat))

    print("Instantiate Class with a, b, c slots:")
    print(timeit("""b = Test(1,2,3)""", """from __main__ import Test""", number=nrepeat))

    print("Instantiate Tuple with 3 values:")
    print(timeit("""c = (1,2,3)""", """from __main__ import Test""", number=nrepeat))

    print("\n=== Read ===\n")

    print("Access NamedTuple by name:")
    print(timeit("z = a.c", "from __main__ import a"))

    print("Access NamedTuple by index:")
    print(timeit("z = a[2]", "from __main__ import a"))

    print("Access slots Class by name:")
    print(timeit("z = b.c", "from __main__ import b"))

    print("Access Tuple by index:")
    print(timeit("z = d[2]", "from __main__ import d"))
