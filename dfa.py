import numpy as np
import matplotlib.pyplot as plt

# detrended fluctuation analysis

def calc_rms(x, scale):
    print x.shape[0], scale
    shape = (x.shape[0]//scale, scale)
    X = np.lib.stride_tricks.as_strided(x,shape=shape)
    scale_ax = np.arange(scale)
    rms = np.zeros(X.shape[0])
    for e, xcut in enumerate(X):
        coeff = np.polyfit(scale_ax, xcut, 1)
        xfit = np.polyval(coeff, scale_ax)
        rms[e] = np.sqrt(np.mean((xcut-xfit)**2))
    return rms

def dfa(x, scale_lim=[3,10], scale_dens=0.25, show=False):
    y = np.cumsum(x - np.mean(x))
    scales = (2**np.arange(scale_lim[0], scale_lim[1], scale_dens)).astype(np.int)
    fluct = np.zeros(len(scales))
    for e, sc in enumerate(scales):
        fluct[e] = np.mean(np.sqrt(calc_rms(y, sc)**2))
    coeff = np.polyfit(np.log2(scales), np.log2(fluct))
    if show:
        plt.plot(scales, fluct, 'r', label='$\alpha$ = %0.2f'%coeff[0])
        plt.title('DFA')
        plt.xlabel('$log_{10}$(time window)')
        plt.ylabel('$log_{10}$<F(t)>')
    return scales, fluct, coeff[0]


x = np.random.randn(1000)
dfa(x)
