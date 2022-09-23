from multiprocessing import Manager
from utils import print_results, time_statement_ex

MY_GLOBAL_PI = 3.1415  # global variable #1
MY_GLOBAL_E = 2.7182   # global variable #2


def one_global_in_loop():
    """Use of one single global variable in a for loop."""
    value = 0
    for i in range(100_000):
        value += i * MY_GLOBAL_PI * 2.7182


def two_globals_in_loop():
    """Use of 2 global variables in a for loop."""
    value = 0
    for i in range(100_000):
        value += i * MY_GLOBAL_PI * MY_GLOBAL_E


def no_globals_in_loop():
    """Use values in for loop."""
    value = 0
    for i in range(100_000):
        value += i * 3.1415 * 2.7182


def copy_globals_in_loop():
    """Use locals copy in for loop."""
    value = 0
    pi = MY_GLOBAL_PI
    e = MY_GLOBAL_E
    for i in range(100_000):
        value += i * pi * e


# bench builtin vs global vs local functions

GLEN = len  # a global reference to builtin function


def builtin_function():
    """call builtin function in for loop."""
    for i in range(100_000):
        len('abcde')


def global_function_ref():
    """call global reference to builtin function."""
    for i in range(100_000):
        GLEN('abcde')


def local_function_ref():
    """call local reference to builtin function."""
    name = len
    for i in range(100_000):
        name('abcde')


if __name__ == "__main__":
    manager = Manager()
    return_dict = manager.dict()
    loop = 100
    time_statement_ex("one_global_in_loop()", "from bench_globals import one_global_in_loop", loop, return_dict)
    time_statement_ex("two_globals_in_loop()", "from bench_globals import two_globals_in_loop", loop, return_dict)
    time_statement_ex("no_globals_in_loop()", "from bench_globals import no_globals_in_loop", loop, return_dict)
    time_statement_ex("copy_globals_in_loop()", "from bench_globals import copy_globals_in_loop", loop, return_dict)
    print_results(return_dict, loop)
    return_dict.clear()

    print("bench builtin vs global vs local function\n")
    time_statement_ex("builtin_function()", "from bench_globals import builtin_function", loop, return_dict)
    time_statement_ex("global_function_ref()", "from bench_globals import global_function_ref", loop, return_dict)
    time_statement_ex("local_function_ref()", "from bench_globals import local_function_ref", loop, return_dict)
    print_results(return_dict, loop)
