
# Unigram LM with Jelinek-Mercer smoothing

For λ = 0.9

```
Queryid (Num):       25
Total number of documents over all queries
    Retrieved:    25000
    Relevant:      1832
    Rel_ret:        890
Interpolated Recall - Precision Averages:
    at 0.00       0.5119
    at 0.10       0.3445
    at 0.20       0.2761
    at 0.30       0.2172
    at 0.40       0.1844
    at 0.50       0.1425
    at 0.60       0.1285
    at 0.70       0.1133
    at 0.80       0.0904
    at 0.90       0.0628
    at 1.00       0.0158
Average precision (non-interpolated) for all rel docs(averaged over queries)
                  0.1709
Precision:
  At    5 docs:   0.2480
  At   10 docs:   0.2400
  At   15 docs:   0.2213
  At   20 docs:   0.2160
  At   30 docs:   0.2160
  At  100 docs:   0.1544
  At  200 docs:   0.1076
  At  500 docs:   0.0616
  At 1000 docs:   0.0356
R-Precision (precision after R (= num_rel for a query) docs retrieved):
    Exact:        0.1991
```

For λ = 0.5

```
Queryid (Num):       25
Total number of documents over all queries
    Retrieved:    25000
    Relevant:      1832
    Rel_ret:        949
Interpolated Recall - Precision Averages:
    at 0.00       0.4923
    at 0.10       0.3277
    at 0.20       0.2784
    at 0.30       0.2510
    at 0.40       0.2019
    at 0.50       0.1673
    at 0.60       0.1534
    at 0.70       0.1322
    at 0.80       0.1029
    at 0.90       0.0819
    at 1.00       0.0220
Average precision (non-interpolated) for all rel docs(averaged over queries)
                  0.1851
Precision:
  At    5 docs:   0.3120
  At   10 docs:   0.2640
  At   15 docs:   0.2560
  At   20 docs:   0.2420
  At   30 docs:   0.2333
  At  100 docs:   0.1644
  At  200 docs:   0.1160
  At  500 docs:   0.0618
  At 1000 docs:   0.0380
R-Precision (precision after R (= num_rel for a query) docs retrieved):
    Exact:        0.2106
```

For λ = 0.2

```
Queryid (Num):       25
Total number of documents over all queries
    Retrieved:    25000
    Relevant:      1832
    Rel_ret:        962
Interpolated Recall - Precision Averages:
    at 0.00       0.4762
    at 0.10       0.3344
    at 0.20       0.2825
    at 0.30       0.2639
    at 0.40       0.2284
    at 0.50       0.1999
    at 0.60       0.1637
    at 0.70       0.1426
    at 0.80       0.1111
    at 0.90       0.0772
    at 1.00       0.0268
Average precision (non-interpolated) for all rel docs(averaged over queries)
                  0.1946
Precision:
  At    5 docs:   0.2880
  At   10 docs:   0.2840
  At   15 docs:   0.2587
  At   20 docs:   0.2660
  At   30 docs:   0.2413
  At  100 docs:   0.1652
  At  200 docs:   0.1132
  At  500 docs:   0.0622
  At 1000 docs:   0.0385
R-Precision (precision after R (= num_rel for a query) docs retrieved):
    Exact:        0.2069
```


For λ = 0.1

```
Queryid (Num):       25
Total number of documents over all queries
    Retrieved:    25000
    Relevant:      1832
    Rel_ret:        927
Interpolated Recall - Precision Averages:
    at 0.00       0.4638
    at 0.10       0.3355
    at 0.20       0.2840
    at 0.30       0.2690
    at 0.40       0.2369
    at 0.50       0.2060
    at 0.60       0.1594
    at 0.70       0.1338
    at 0.80       0.1046
    at 0.90       0.0658
    at 1.00       0.0274
Average precision (non-interpolated) for all rel docs(averaged over queries)
                  0.1926
Precision:
  At    5 docs:   0.2800
  At   10 docs:   0.2800
  At   15 docs:   0.2587
  At   20 docs:   0.2600
  At   30 docs:   0.2427
  At  100 docs:   0.1612
  At  200 docs:   0.1094
  At  500 docs:   0.0598
  At 1000 docs:   0.0371
R-Precision (precision after R (= num_rel for a query) docs retrieved):
    Exact:        0.2014
```
