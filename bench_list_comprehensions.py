"""
# List comprehensions

Used to create a new list from an iterable, either to filter or to map the elements.
Please note that you can also use comprehensions for sets and dicts.

Bonus: you will find around recommendations telling you to use generator expressions instead of list comprehensions.

## What is a list comprehension ?

A list comprehension is a specific python syntax to express a for loop expression:

new_list = []
for x in iterable:
  if condition(x):
    new_list.append(operation(x))

Once you have your elements from the for expression, you can format them as a list comprehension:

new_list = [operation(x) for x in old_list if condition(x)]


People usually complain that list comprehensions are less readable. But imho, this is mostly because people tend
to write them on one single line. List comprehensions are composed of 3 parts and you can write them on
multiple lines:

new_list = [
    operation(x)         # <- part 1: the operation
    for x in old_list    # <- part 2: the loop
    if condition(x)      # <- part 3: the condition
]


And in case of multiple loops:

flattened = []
for row in matrix:
    for x in row:
        flattened.append(operation(x))

using list comprehensions:

flattened = [
    x
    for row in matrix
    for x in row
]
"""
from multiprocessing import Manager, Process
from utils import time_statement_ex, print_results


def filter_with_for():
    result = []
    inputs = range(100_000)
    for n in inputs:
        if n % 2:
            result.append(n)


def filter_with_list_comprehension():
    inputs = range(100_000)
    result = [n for n in inputs if n % 2]


def filter_with_list_comprehension_ml():
    inputs = range(100_000)
    result = [
        n                    # <- part 1: operation
        for n in inputs      # <- part 2: loop
        if n % 2             # <- part 3: condition
    ]


def join_with_generator():
    words = ["Lorem" "ipsum" "dolor" "sit" "amet" "consectetur" "adipiscing" "elit" "eiusmod" "tempor"]
    for x in range(100_000):
        # by default when u pass a comprehension expression to a function it creates a generator expression
        # i.e. no need to wrap the expression with brackets
        ''.join(word.upper() for word in words)


def join_with_list():
    words = ["Lorem" "ipsum" "dolor" "sit" "amet" "consectetur" "adipiscing" "elit" "eiusmod" "tempor"]
    for x in range(100_000):
        # if you wrap the comprehension expression into square brackets then it creates a new list
        ''.join([word.upper() for word in words])


if __name__ == "__main__":
    manager = Manager()
    return_dict = manager.dict()
    loop = 100
    time_statement_ex("filter_with_for()",
                      "from __main__ import filter_with_for", loop, return_dict)
    time_statement_ex("filter_with_list_comprehension()",
                      "from __main__ import filter_with_list_comprehension", loop, return_dict)
    time_statement_ex("filter_with_list_comprehension_ml()",
                      "from __main__ import filter_with_list_comprehension_ml", loop, return_dict)
    print_results(return_dict, loop)
    return_dict.clear()
    # bench generator expression vs list comprehension
    print()

    loop = 10
    time_statement_ex("join_with_generator()",
                      "from __main__ import join_with_generator", loop, return_dict)
    time_statement_ex("join_with_list()",
                      "from __main__ import join_with_list", loop, return_dict)
    print_results(return_dict, loop)
