"""Below is the small benchmark ran by Python core developer Serhiy Storchaka to assess the improvement made to f-strings
```
python -mtimeit -s 'x = 42' '"%s-" % x'
python -mtimeit -s 'x = 42' 'f"{x}-"'
python -mtimeit -s 'x = "42"' 'f"{x}{x}"'
python -mtimeit -s 'x = "42"' '"%s%s" % (x,x)'
python -mtimeit -s 'x = "42"' '"".join((x, x))'
```
"""
from multiprocessing import Manager, Process
from timeit import Timer
from sys import version

try:
    from statistics import fmean
except ImportError:
    from statistics import mean as fmean

print(f"Python version: {version}")

LOOP = 10**6
SETUP = "a = 'beautiful'; b = 'simplicity'; c = 'gratitude'; d = 'strong'; e = 'satisfaction'; f = 'happy'"

STATEMENTS2 = [
    "a + b",
    "f'{a}{b}'",
    "''.join((a, b))",
    "'%s%s' % (a, b)",
    "'{0}{1}'.format(a, b)"
]

STATEMENTS3 = [
    "a + b + c",
    "f'{a}{b}{c}'",
    "''.join((a, b, c))",
    "'%s%s%s' % (a, b, c)",
    "'{0}{1}{2}'.format(a, b, c)"
]

STATEMENTS6 = [
    "a + b + c + d + e + f",
    "f'{a}{b}{c}{d}{e}{f}'",
    "''.join((a, b, c, d, e, f))",
    "'%s%s%s%s%s%s' % (a, b, c, d, e, f)",
    "'{0}{1}{2}{3}{4}{5}'.format(a, b, c, d, e, f)"
]

STATEMENTS_WRAP_SPACES = [
    "' ' + a + ' '",
    "f' {a} '"
]


def time_statement(statement, loop, return_dict):
    tmr = Timer(statement, setup=SETUP)
    results = tmr.repeat(repeat=5, number=loop)
    # print(f"{statement}: {loop} loops, repeat=5, min: {min(results)}, mean: {fmean(results)}, max:{max(results)}")
    # print(f"{loop} loops, repeat=5, min: {min(results)/loop*10**9} nsec per loop")
    return_dict[statement] = results


def _print_results(results):
    import operator
    precision = 10**6
    # new columns test|min|mean|max|loop   (10**9: loop time in nsec)
    results_ex = [(k, min(v), fmean(v), max(v), min(v)/LOOP*10**9) for k, v in results.items()]
    # sort results by min loop time
    sorted_result_ex = sorted(results_ex, key=lambda x: x[4])
    # new results with diff time %
    results_diff = [("Test", "Min", "Mean", "Max", "Loop (nsec)", "% Slower")]
    fastest = sorted_result_ex[0][4]
    for i in sorted_result_ex:
        diff = ((fastest - i[4]) / fastest) * 100
        results_diff.append((*i, round(diff, 2)))

    # pretty print
    for r in results_diff:
        print(f"{r[0]:<30}{r[1]:<30}{r[2]:<30}{r[3]:<30}{r[4]:<30}{r[5]}")

    print()


if __name__ == '__main__':

    manager = Manager()
    return_dict = manager.dict()

    for stmt in STATEMENTS2:
        # we run time_statement in a subprocess to avoid any kind of string optimization that could influence other runs
        p = Process(target=time_statement, args=(stmt, LOOP, return_dict))
        p.start()
        p.join()

    print(f"{LOOP} loops test results:\n")
    _print_results(return_dict)

    return_dict.clear()
    for stmt in STATEMENTS3:
        # we run time_statement in a subprocess to avoid any kind of string optimization that could influence other runs
        p = Process(target=time_statement, args=(stmt, 100000, return_dict))
        p.start()
        p.join()
    _print_results(return_dict)

    return_dict.clear()
    for stmt in STATEMENTS6:
        # we run time_statement in a subprocess to avoid any kind of string optimization that could influence other runs
        p = Process(target=time_statement, args=(stmt, 100000, return_dict))
        p.start()
        p.join()
    _print_results(return_dict)

    return_dict.clear()
    for stmt in STATEMENTS_WRAP_SPACES:
        # we run time_statement in a subprocess to avoid any kind of string optimization that could influence other runs
        p = Process(target=time_statement, args=(stmt, 100000, return_dict))
        p.start()
        p.join()
    _print_results(return_dict)

