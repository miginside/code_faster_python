# Code faster Python
  * [bench_data_structures.py](#bench_data_structurespy): compare speed between data structures.
  * [bench_tiny_functions.py](#bench_tiny_functionspy): assess speed impact of calling tiny functions.
  * [bench_string_concatenation.py](#bench_string_concatenationpy): compare string concatenations.
  * [bench_list_comprehensions.py](#bench_list_comprehensionspy): for loops vs list comprehensions
  * [bench_globals.py](#bench_globalspy): impact of using global variables in large loops


**Remarks:**
  * Scripts are executed with optimization flags `-O`.
    * Do not use `-OO` as it will slow the timeit call 
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

## bench_string_concatenation.py

#### Results on RHEL 7.6 - Intel(R) Xeon(R) Platinum 8270 CPU @ 2.70GHz
* Python 3.6:
```
Python version: 3.6.3 (default, Jan  9 2018, 10:19:07)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)]
1000000 loops test results:

Test                          Min                           Mean                          Max                           Loop                          % Slower
a + b                         0.05470552295446396           0.054811692237854             0.054983556270599365          54.70552295446396             0.0
f'{a}{b}'                     0.06454875320196152           0.0646488681435585            0.06469856947660446           64.54875320196152             -17.99
''.join((a, b))               0.11484682559967041           0.11506029516458512           0.11533346772193909           114.84682559967041            -109.94
'%s%s' % (a, b)               0.14325429499149323           0.14332662522792816           0.143397755920887             143.25429499149323            -161.86
'{0}{1}'.format(a, b)         0.2624841406941414            0.2672045439481735            0.2734183669090271            262.4841406941414             -379.81

Test                          Min                           Mean                          Max                           Loop                          % Slower
f'{a}{b}{c}'                  0.007667466998100281          0.007684372365474701          0.0077038779854774475         7.667466998100281             0.0
a + b + c                     0.009904667735099792          0.009949156641960144          0.010016322135925293          9.904667735099792             -29.18
''.join((a, b, c))            0.012553088366985321          0.012591679394245148          0.012653343379497528          12.553088366985321            -63.72
'%s%s%s' % (a, b, c)          0.01683187484741211           0.016960838437080385          0.01709858328104019           16.83187484741211             -119.52
'{0}{1}{2}'.format(a, b, c)   0.030627645552158356          0.030699703097343444          0.03085419535636902           30.627645552158356            -299.45

Test                          Min                           Mean                          Max                           Loop                          % Slower
f'{a}{b}{c}{d}{e}{f}'         0.011414431035518646          0.011456316709518433          0.0114816352725029            11.414431035518646            0.0
''.join((a, b, c, d, e, f))   0.01555914431810379           0.015613898634910583          0.01563902199268341           15.559144318103789            -36.31
a + b + c + d + e + f         0.02383860945701599           0.023870931565761568          0.023919709026813507          23.83860945701599             -108.85
'%s%s%s%s%s%s' % (a, b, c, d, e, f)0.023952066898345947          0.023987901210784913          0.02407432347536087           23.952066898345947            -109.84
'{0}{1}{2}{3}{4}{5}'.format(a, b, c, d, e, f)0.050849564373493195          0.050872088968753816          0.05089103430509567           50.849564373493195            -345.48

Test                          Min                           Mean                          Max                           Loop                          % Slower
f' {a} '                      0.006960593163967133          0.0070200666785240175         0.007053166627883911          6.960593163967133             0.0
' ' + a + ' '                 0.008654072880744934          0.008674402534961701          0.008696384727954865          8.654072880744934             -24.33
```


* Python 3.9:
```
Python version: 3.9.7 (default, Oct 26 2021, 21:38:35)
[GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]
1000000 loops test results:

Test                          Min                           Mean                          Max                           Loop                          % Slower
a + b                         0.04411395639181137           0.04440985769033432           0.04470551759004593           44.11395639181137             0.0
f'{a}{b}'                     0.05397985875606537           0.05411034375429154           0.05419803410768509           53.97985875606537             -22.36
''.join((a, b))               0.08768166601657867           0.09301978349685669           0.11381072551012039           87.68166601657867             -98.76
'%s%s' % (a, b)               0.11535204946994781           0.11545586436986924           0.11557368189096451           115.35204946994781            -161.49
'{0}{1}'.format(a, b)         0.18229172378778458           0.1825376495718956            0.183050736784935             182.29172378778458            -313.23

Test                          Min                           Mean                          Max                           Loop                          % Slower
f'{a}{b}{c}'                  0.006467908620834351          0.00648694783449173           0.006500966846942902          6.467908620834351             0.0
a + b + c                     0.007581301033496857          0.007657288014888764          0.007750451564788818          7.581301033496856             -17.21
''.join((a, b, c))            0.009563125669956207          0.009596903622150422          0.009638711810112             9.563125669956207             -47.85
'%s%s%s' % (a, b, c)          0.013055123388767242          0.013080953061580658          0.013132870197296143          13.055123388767242            -101.84
'{0}{1}{2}'.format(a, b, c)   0.0220322385430336            0.02204275131225586           0.02205493301153183           22.0322385430336              -240.64

Test                          Min                           Mean                          Max                           Loop                          % Slower
f'{a}{b}{c}{d}{e}{f}'         0.009174764156341553          0.009212754666805267          0.009234368801116943          9.174764156341553             0.0
''.join((a, b, c, d, e, f))   0.011653050780296326          0.011717493832111358          0.01173960417509079           11.653050780296326            -27.01
'%s%s%s%s%s%s' % (a, b, c, d, e, f)0.01838591694831848           0.018402352929115295          0.018428228795528412          18.38591694831848             -100.4
a + b + c + d + e + f         0.019724123179912567          0.01975693553686142           0.019778206944465637          19.724123179912567            -114.98
'{0}{1}{2}{3}{4}{5}'.format(a, b, c, d, e, f)0.033394262194633484          0.033604615926742555          0.03384295105934143           33.394262194633484            -263.98

Test                          Min                           Mean                          Max                           Loop                          % Slower
f' {a} '                      0.0057670921087265015         0.005823546648025512          0.005848944187164307          5.7670921087265015            0.0
' ' + a + ' '                 0.007373899221420288          0.007395625114440918          0.00743701308965683           7.373899221420288             -27.86
```

* Python 3.10:
```
Python version: 3.10.4 (main, Jun  9 2022, 17:43:11) [GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]
1000000 loops test results:

Test                          Min                           Mean                          Max                           Loop                          % Slower
a + b                         0.0426311194896698            0.0428151935338974            0.04302166402339935           42.6311194896698              0.0
f'{a}{b}'                     0.05976872146129608           0.059849601984024045          0.05994449555873871           59.76872146129608             -40.2
''.join((a, b))               0.09638112038373947           0.0967095747590065            0.09752564132213593           96.38112038373947             -126.08
'%s%s' % (a, b)               0.13060258328914642           0.13117226511240004           0.13195807486772537           130.60258328914642            -206.36
'{0}{1}'.format(a, b)         0.17392181605100632           0.17627356052398682           0.1834035962820053            173.92181605100632            -307.97

Test                          Min                           Mean                          Max                           Loop                          % Slower
f'{a}{b}{c}'                  0.007332198321819305          0.0073852971196174625         0.007423952221870422          7.332198321819305             0.0
a + b + c                     0.007341928780078888          0.007380229234695434          0.007411673665046692          7.341928780078888             -0.13
''.join((a, b, c))            0.010686658322811127          0.0106992706656456            0.010734565556049347          10.686658322811127            -45.75
'%s%s%s' % (a, b, c)          0.014610156416893005          0.014664334058761597          0.014707125723361969          14.610156416893005            -99.26
'{0}{1}{2}'.format(a, b, c)   0.021433040499687195          0.021442775428295136          0.0214739590883255            21.433040499687195            -192.31

Test                          Min                           Mean                          Max                           Loop                          % Slower
f'{a}{b}{c}{d}{e}{f}'         0.011854954063892365          0.011895620822906494          0.011939264833927155          11.854954063892365            0.0
''.join((a, b, c, d, e, f))   0.014480262994766235          0.014496071636676789          0.014513552188873291          14.480262994766235            -22.15
a + b + c + d + e + f         0.019312456250190735          0.019345021247863768          0.01940333843231201           19.312456250190735            -62.91
'%s%s%s%s%s%s' % (a, b, c, d, e, f)0.02037166804075241           0.020453740656375886          0.02053602784872055           20.37166804075241             -71.84
'{0}{1}{2}{3}{4}{5}'.format(a, b, c, d, e, f)0.033759258687496185          0.03377431035041809           0.03381109982728958           33.759258687496185            -184.77

Test                          Min                           Mean                          Max                           Loop                          % Slower
f' {a} '                      0.005997739732265472          0.006023126840591431          0.006056338548660278          5.997739732265472             0.0
' ' + a + ' '                 0.007245957851409912          0.007262611389160156          0.0072799548506736755         7.245957851409912             -20.81
```

## bench_list_comprehensions.py

#### Results on RHEL 7.6 - Intel(R) Xeon(R) Platinum 8270 CPU @ 2.70GHz

* Python 3.9:
```
Python version: 3.9.7 (default, Oct 26 2021, 21:38:35)
[GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]

100 loops test results:
Test                                    Min (s)     Mean (s)    Max (s)     Loop (msec) % Slower
filter_with_list_comprehension_ml()     0.4837      0.48476     0.48661     4.83696     0.0
filter_with_list_comprehension()        0.48553     0.48806     0.49074     4.85533     0.38
filter_with_for()                       0.60401     0.6064      0.61077     6.04013     24.87


10 loops test results:
Test                                    Min (s)     Mean (s)    Max (s)     Loop (msec) % Slower
join_with_list()                        0.28209     0.28245     0.28319     28.20949    0.0
join_with_generator()                   0.40213     0.40215     0.40221     40.21257    42.55
```

* Python 3.10:
```
Python version: 3.10.4 (main, Jun  9 2022, 17:43:11) [GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]

100 loops test results:
Test                                    Min (s)     Mean (s)    Max (s)     Loop (msec) % Slower
filter_with_list_comprehension()        0.48361     0.48583     0.48771     4.83615     0.0
filter_with_list_comprehension_ml()     0.48383     0.5047      0.5822      4.83833     0.05
filter_with_for()                       0.59127     0.59229     0.59376     5.91274     22.26


10 loops test results:
Test                                    Min (s)     Mean (s)    Max (s)     Loop (msec) % Slower
join_with_list()                        0.29744     0.30162     0.3039      29.74421    0.0
join_with_generator()                   0.40408     0.40417     0.40435     40.40797    35.85

```

## bench_globals.py

#### Results on RHEL 7.6 - Intel(R) Xeon(R) Platinum 8270 CPU @ 2.70GHz

* Python 3.9:
```
Python version: 3.9.7 (default, Oct 26 2021, 21:38:35)
[GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]

100 loops test results:
Test                                    Min (s)     Mean (s)    Max (s)     Loop (msec) % Slower
copy_globals_in_loop()                  0.72062     0.72188     0.723       7.20616     0.0
no_globals_in_loop()                    0.73927     0.74116     0.74423     7.39266     2.59
one_global_in_loop()                    0.79159     0.79373     0.79562     7.91588     9.85
two_globals_in_loop()                   0.85044     0.85255     0.85665     8.50443     18.02

bench builtin vs global vs local function

Python version: 3.9.7 (default, Oct 26 2021, 21:38:35)
[GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]

100 loops test results:
Test                                    Min (s)     Mean (s)    Max (s)     Loop (msec) % Slower
local_function_ref()                    0.38121     0.38253     0.38516     3.81213     0.0
global_function_ref()                   0.47564     0.48468     0.52        4.7564      24.77
builtin_function()                      0.55434     0.55506     0.55588     5.54339     45.41
```

* Python 3.10:
```
Python version: 3.10.4 (main, Jun  9 2022, 17:43:11) [GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]

100 loops test results:
Test                                    Min (s)     Mean (s)    Max (s)     Loop (msec) % Slower
no_globals_in_loop()                    0.66022     0.66104     0.66364     6.60218     0.0
copy_globals_in_loop()                  0.66228     0.67079     0.68481     6.62275     0.31
one_global_in_loop()                    0.77621     0.77716     0.77772     7.76208     17.57
two_globals_in_loop()                   0.84514     0.84593     0.84677     8.4514      28.01 

bench builtin vs global vs local function

Python version: 3.10.4 (main, Jun  9 2022, 17:43:11) [GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]

100 loops test results:
Test                                    Min (s)     Mean (s)    Max (s)     Loop (msec) % Slower
local_function_ref()                    0.33767     0.33797     0.33835     3.37671     0.0
global_function_ref()                   0.45228     0.45248     0.4527      4.52277     33.94
builtin_function()                      0.483       0.48373     0.48449     4.83001     43.04
```
