from multiprocessing import Process
from statistics import fmean
from timeit import Timer
from sys import version


def time_statement(statement, setup, loop, return_dict):
    tmr = Timer(statement, setup=setup)
    results = tmr.repeat(repeat=5, number=loop)
    if __debug__:
        print(f"{statement}: {loop} loops, repeat=5, min: {min(results)}, mean: {fmean(results)}, max:{max(results)}")
        print(f"{loop} loops, repeat=5, min: {min(results)*10**3/loop} msec per loop")
    return_dict[statement] = results


def time_statement_ex(statement, setup, loop, return_dict):
    p = Process(target=time_statement, args=(statement, setup, loop, return_dict))
    p.start()
    p.join()


def print_results(results, loop):
    print(f"Python version: {version}\n")
    print(f"{loop} loops test results:")
    # new columns test|min|mean|max|loop   (10**9: loop time in nsec)
    results_ex = [(k, min(v), fmean(v), max(v), min(v)*10**3/loop) for k, v in results.items()]
    # sort results by min loop time
    sorted_result_ex = sorted(results_ex, key=lambda x: x[4])
    # new results with diff time %
    results_diff = [("Test", "Min (s)", "Mean (s)", "Max (s)", "Loop (msec)", "% Slower")]
    fastest = sorted_result_ex[0][4]
    for i in sorted_result_ex:
        diff = ((fastest - i[4]) / fastest) * 100
        results_diff.append((i[0], round(i[1], 5), round(i[2], 5), round(i[3], 5), round(i[4], 5), abs(round(diff, 2))))

    # pretty print
    for r in results_diff:
        print(f"{r[0]:<40}{r[1]:<12}{r[2]:<12}{r[3]:<12}{r[4]:<12}{r[5]}")

    print()
