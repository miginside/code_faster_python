# Code faster Python
  * **bench_data_structures.py**: compare speed between collections.namedtuple, class with slots and a bare tuple.
  * **bench_tiny_functions.py**: assess speed impact of calling tiny functions


## bench_data_structures.py

Results on an Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz (4 cores):
* Python 3.9:
```
=== Definition ===

Define NamedTuple with a, b, c:
3.9061675
Define Class with slots a, b, c:
0.5140005000000007
Define Tuple with 3 values:
0.0007945000000004754

=== Instantiation ===

Instantiate NamedTuple with a, b, c:
4.1665896
Instantiate Class with slots a, b, c:
2.0201188000000005
Instantiate Tuple with 3 values:
0.14583939999999984

=== Read ===

Access NamedTuple attribute by name:
0.33739650000000054
Access NamedTuple attribute by index:
0.27850080000000155
Access Class slots by name:
0.3994631000000002
Access Tuple by index:
0.0632085
```

## bench_tiny_functions.py

Results on an Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz (4 cores):
* Python 3.9:
```
call tiny function, loop=1000:
7.1489971
call inline function, loop=1000:
3.147498100000001 (55.97% faster)
call 2x tiny function, loop=1000:
13.2962043
call 2x inline function, loop=1000:
5.207785000000001 (60.83% faster)
```