Detrended Fluctuation Analysis
==============================

Simple python implementation of DFA algorithm.
It bases on these two articles:

* Hardstone, R. et al. Detrended fluctuation analysis: A scale-free view on neuronal oscillations. Front. Physiol. 3 NOV, 1–13 (2012).
* Ihlen, E. a F. Introduction to multifractal detrended fluctuation analysis in Matlab. Front. Physiol. 3 JUN, 1–18 (2012).

You may test it using power law data generator from `generate.py`, or using code below:

```python
from dfa import dfa
from generate import power_law_noise

x = power_law_noise(2**12, 0.8)
scales, fluct, alpha = dfa(x)
print("DFA exponent {}: {}".format(e+1, alpha))

```

Requirements
------------

* numpy
* matplotlib
