from collections import namedtuple

MyNamedTuple = namedtuple('TEST', 'a b c')
my_named_tuple = MyNamedTuple(a=1,b=2,c=3)

class ClassWithSlots():
    __slots__ = ['a','b','c']
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

class_with_slots = ClassWithSlots(1,2,3)

my_tuple = ('a','b','c')

if __name__ == '__main__':
    from timeit import timeit
    nrepeat = 10**5

    print("=== Definition ===\n")
    print("Define NamedTuple with a, b, c:")
    print(timeit("""\
MyNamedTuple = namedtuple('TEST', 'a b c')""", """\
from collections import namedtuple""", number=nrepeat))

    print("Define Class with slots a, b, c:")
    print(timeit("""\
class ClassWithSlots(object):
    __slots__ = ['a','b','c']
def __init__(self, a, b, c):
    self.a=a
    self.b=b
    self.c=c""", number=nrepeat))

    print("Define Tuple with 3 values:")
    print(timeit("('a','b','c')", number=nrepeat))


    print("\n=== Instantiation ===\n")
    nrepeat=10**7

    print("Instantiate NamedTuple with a, b, c:")
    print(timeit("a = MyNamedTuple(a=1,b=2,c=3)", "from __main__ import MyNamedTuple", number=nrepeat))

    print("Instantiate Class with slots a, b, c:")
    print(timeit("b = ClassWithSlots(1,2,3)", "from __main__ import ClassWithSlots", number=nrepeat))

    print("Instantiate Tuple with 3 values:")
    print(timeit("c = (1,2,3)", number=nrepeat))


    print("\n=== Read ===\n")
    nrepeat=10**7

    print("Access NamedTuple attribute by name:")
    print(timeit("z = my_named_tuple.c", "from __main__ import my_named_tuple", number=nrepeat))

    print("Access NamedTuple attribute by index:")
    print(timeit("z = my_named_tuple[2]", "from __main__ import my_named_tuple", number=nrepeat))

    print("Access Class slots by name:")
    print(timeit("z = class_with_slots.c", "from __main__ import class_with_slots", number=nrepeat))

    print("Access Tuple by index:")
    print(timeit("z = my_tuple[2]", "from __main__ import my_tuple"))

    print()
    