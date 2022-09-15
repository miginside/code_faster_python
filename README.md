# Code faster Python
  * **bench_data_structures.py**: compare speed between data structures.
  * **bench_tiny_functions.py**: assess speed impact of calling tiny functions.

**Remarks:**
  * Scripts are executed with optimization flags `-OO`.
  * Differences <1% are not significant. 

## bench_data_structures.py

Results on Win10 - Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz (4 cores):
* Python 3.9:
```
```

* Python 3.10:
```
```

Results on RHEL 7.6 - Intel(R) Xeon(R) Platinum 8270 CPU @ 2.70GHz
* Python 3.9:
```
Test                                         Time                          % Slower
Define a tuple type                          0.015219852328300476          0.0
Define simple class                          0.5656654536724091            -3616.6290544132635
Define class with slots                      0.5838318914175034            -3735.9891990009664
Define collections.namedtuple                3.5693187415599823            -23351.730441057112
Define typing.NamedTuple                     4.667198687791824             -30565.203492897406
Define dataclass                             26.506394058465958            -174056.70984651262

Test                                         Time                          % Slower
Instantiate tuple                            0.10374129563570023           0.0
Instantiate class with slots                 3.009273499250412             -2800.747943054259
Instantiate simple class                     3.4557953849434853            -3231.166594524631
Instantiate dataclass                        3.4735378846526146            -3248.2692339320224
Instantiate collections.namedtuple           3.778028555214405             -3541.7788423246584
Instantiate typing.NamedTuple                3.7814667746424675            -3545.093066816452

Test                                         Time                          % Slower
access tuple by index                        2.202527701854706             0.0
access typing.NamedTuple member by index     2.2076380029320717            -0.2320198321711273
access collections.namedtuple by index       2.2099881172180176            -0.33872061436637085
access typing.NamedTuple member              2.214505635201931             -0.5438266831849063
access collections.namedtuple member         2.261020377278328             -2.6557066852946543
access class with slots member               2.429688647389412             -10.313647603315875
access simple class member                   2.5912359431385994            -17.64827933635386
access dataclass member                      2.6616512686014175            -20.845302711066594
```

* Python 3.10:
```
Test                                         Time                          % Slower
Define a tuple type                          0.017090246081352234          0.0
Define simple class                          0.5274581164121628            -2986.31083426991
Define class with slots                      0.5535089895129204            -3138.7420688861434
Define collections.namedtuple                3.2708952203392982            -19038.9591745451
Define typing.NamedTuple                     4.404006741940975             -25669.124218441426
Define dataclass                             26.86242362856865             -157079.85276923064

Test                                         Time                          % Slower
Instantiate tuple                            0.1126270666718483            0.0
Instantiate class with slots                 2.6055140867829323            -2213.3995794939706
Instantiate dataclass                        3.089305602014065             -2642.9513111755864
Instantiate simple class                     3.1076595783233643            -2659.247550482587
Instantiate collections.namedtuple           3.3076233714818954            -2836.7926105356455
Instantiate typing.NamedTuple                3.327195107936859             -2854.170082073627

Test                                         Time                          % Slower
access tuple by index                        2.1345604583621025            0.0
access collections.namedtuple by index       2.1353385224938393            -0.0364507891396893
access typing.NamedTuple member by index     2.1377072259783745            -0.14741993387653024
access collections.namedtuple member         2.283767819404602             -6.990074254302911
access typing.NamedTuple member              2.332375220954418             -9.267236344483937
access class with slots member               2.445511966943741             -14.567472538127996
access dataclass member                      2.747134305536747             -28.697891632673013
access simple class member                   2.747283637523651             -28.704887545406198
```

## bench_tiny_functions.py

Results on Win10 - Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz (4 cores):
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
* Python 3.10:
```
call tiny function, loop=1000:
8.835000400000354
call inline function, loop=1000:
3.5376467000005505 (59.96% faster)
call 2x tiny function, loop=1000:
18.153919700000188
call 2x inline function, loop=1000:
5.880108600000312 (67.61% faster)
```

Results on RHEL 7.6 - Intel(R) Xeon(R) Platinum 8270 CPU @ 2.70GHz
* Python 3.9:
```
call tiny function, loop=1000:
9.320463128387928
call inline function, loop=1000:
4.163810446858406 (55.33% faster)
call 2x tiny function, loop=1000:
18.366298034787178
call 2x inline function, loop=1000:
6.5700540989637375 (64.23% faster)
```

* Python 3.10:
```
call tiny function, loop=1000:
9.368650607764721
call inline function, loop=1000:
4.310984067618847 (53.99% faster)
call 2x tiny function, loop=1000:
18.53802677243948
call 2x inline function, loop=1000:
6.660353533923626 (64.07% faster)
```
