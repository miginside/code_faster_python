import collections
import sys
import typing
from dataclasses import dataclass

print(f"Python version: {sys.version}")


# Test @dataclass
@dataclass
class ADataClass:
    a: str
    b: int


# Test collections.namedtuple
CollectionNamedTuple = collections.namedtuple('CollectionNamedTuple', 'a b')


# Test typing.NamedTuple
class TypingNamedTuple(typing.NamedTuple):
    a: str
    b: int


# Test simple class - no slots
class SimpleClass:
    def __init__(self, a, b):
        self.a: str = a
        self.b: int = b

    def __repr__(self):
        return f"<SimpleClass a='{self.a}' b={self.b}>"


# Test class with slots
class ClassWithSlots:
    __slots__ = ['a', 'b']

    def __init__(self, a, b):
        self.a: str = a
        self.b: int = b

    def __repr__(self):
        return f"<ClassWithSlots a='{self.a}' b={self.b}>"


# a tuple
TupleType = tuple[str, int]
a_tuple = ('a', 'b')


def _print_results(results):
    import operator
    precision = 10**6

    for prefix in ["define", "instantiate", "access"]:

        sorted_results = sorted([i for i in results.items() if i[0].lower().startswith(prefix)],
                                key=operator.itemgetter(1))
        # header row
        sorted_results_ex = [("Test", "Time", "% Slower")]
        ref_value = sorted_results[0][1]*precision
        # compute percentage decrease
        for i in sorted_results:
            pct = ((ref_value - (i[1]*precision)) / ref_value) * 100
            sorted_results_ex.append((*i, pct))
        # pretty print
        for a, b, c in sorted_results_ex:
            print(f"{a:<45}{b:<30}{c}")

        print()


if __name__ == '__main__':
    from timeit import timeit

    results = collections.OrderedDict()

    #
    # declarations
    #
    loop = 10**5

    results["Define dataclass"] = timeit("""\
@dataclass
class ADataClass:
    a: str
    b: int""", "from dataclasses import dataclass", number=loop)

    results["Define collections.namedtuple"] = timeit("""\
CollectionNamedTuple = collections.namedtuple('CollectionNamedTuple', 'a b')""",
"import collections", number=loop)

    results["Define typing.NamedTuple"] = timeit("""\
class TypingNamedTuple(typing.NamedTuple):
    a: str
    b: int""", "import typing", number=loop)

    results["Define simple class"] = timeit("""\
class SimpleClass:
    def __init__(self, a, b):
        self.a: str = a
        self.b: int = b

    def __repr__(self):
        return f\"<SimpleClass a='{self.a}' b={self.b}>\"""", number=loop)

    results["Define class with slots"] = timeit("""\
class ClassWithSlots:
    __slots__ = ['a', 'b']

    def __init__(self, a, b):
        self.a: str = a
        self.b: int = b
        
    def __repr__(self):
        return f\"<ClassWithSlots a='{self.a}' b={self.b}>\"""", number=loop)

    results["Define a tuple type"] = timeit("""\
TupleType = tuple[str, int]""", number=loop)

    #
    # instantiation
    #
    loop = 10**7

    results["Instantiate dataclass"] = timeit("a = ADataClass(a='dummy', b=999999)",
                                              "from __main__ import ADataClass", number=loop)

    results["Instantiate collections.namedtuple"] = timeit("a = CollectionNamedTuple(a='dummy', b=999999)",
                                                           "from __main__ import CollectionNamedTuple", number=loop)

    results["Instantiate typing.NamedTuple"] = timeit("a = TypingNamedTuple(a='dummy', b=999999)",
                                                      "from __main__ import TypingNamedTuple", number=loop)

    results["Instantiate simple class"] = timeit("a = SimpleClass(a='dummy', b=999999)",
                                                 "from __main__ import SimpleClass", number=loop)

    results["Instantiate class with slots"] = timeit("a = ClassWithSlots(a='dummy', b=999999)",
                                                     "from __main__ import ClassWithSlots", number=loop)

    results["Instantiate tuple"] = timeit("a: TupleType = ('dummy', 999999)",
                                          "from __main__ import TupleType", number=loop)

    #
    # read
    #
    loop = 10**8

    results["access dataclass member"] = timeit("toto = a_data_class.a", """\
from __main__ import ADataClass
a_data_class = ADataClass(a='dummy', b=999999)""", number=loop)

    results["access collections.namedtuple member"] = timeit("toto = collection_namedtuple.a", """\
from __main__ import CollectionNamedTuple
collection_namedtuple = CollectionNamedTuple(a='dummy', b=999999)""", number=loop)

    results["access collections.namedtuple by index"] = timeit("toto = collection_namedtuple[0]", """\
from __main__ import CollectionNamedTuple
collection_namedtuple = CollectionNamedTuple(a='dummy', b=999999)""", number=loop)

    results["access typing.NamedTuple member"] = timeit("toto = a_typing_namedtuple.a", """\
from __main__ import TypingNamedTuple
a_typing_namedtuple = TypingNamedTuple(a='dummy', b=999999)""", number=loop)

    results["access typing.NamedTuple member by index"] = timeit("toto = a_typing_namedtuple[0]", """\
from __main__ import TypingNamedTuple
a_typing_namedtuple = TypingNamedTuple(a='dummy', b=999999)""", number=loop)

    results["access simple class member"] = timeit("toto = a_simple_class.a", """\
from __main__ import SimpleClass
a_simple_class = SimpleClass(a='dummy', b=999999)""", number=loop)

    results["access class with slots member"] = timeit("toto = a_class_with_slots.a", """\
from __main__ import ClassWithSlots
a_class_with_slots = ClassWithSlots(a='dummy', b=999999)""", number=loop)

    results["access tuple by index"] = timeit("toto = a_tuple[0]", """\
a_tuple = ('dummy', 999999)""", number=loop)

    _print_results(results)
