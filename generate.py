# author: Dominik Krzeminski (dokato)

import numpy as np
import matplotlib.pyplot as plt
from dfa import dfa


def power_law_noise(n, alpha, var=1):
    '''
    Generale power law noise. 
    
    Args:
    -----
      *n* : int
        number of data points
      *alpha* : float
        DFA exponent
      *var* = 1 : float
        variance
    Returns:
    --------
      *x* : numpy.array
        generated noisy data with exponent *alpha*

    Based on:
    N. Jeremy Kasdin, Discrete simulation of power law noise (for
    oscillator stability evaluation)
    '''
    # computing standard deviation from variance
    stdev = np.sqrt(np.abs(var))
    
    beta = 2*alpha-1
    
    hfa = np.zeros(2*n)
    hfa[0] = 1
    for i in range(1,n):
        hfa[i] = hfa[i-1] * (0.5*beta + (i-1))/i
    
    # sample white noise
    wfa = np.hstack((-stdev +2*stdev * np.random.rand(n), np.zeros(n)))
    
    fh = np.fft.fft(hfa)
    fw = np.fft.fft(wfa)
    
    fh = fh[1:n+1]
    fw = fw[1:n+1]
    
    ftot = fh * fw
    
    # matching the conventions of the Numerical Recipes
    
    ftot = np.hstack((ftot, np.zeros(n-1)))
    
    x = np.fft.ifft(ftot)
    
    return np.real(x[:n])

if __name__=='__main__':
    x1 = power_law_noise(2**12, 0.5)
    x2 = power_law_noise(2**12, 0.8)
    x3 = power_law_noise(2**12, 1.2)

    plt.subplot(311)
    plt.plot(x1)
    plt.subplot(312)
    plt.plot(x2)
    plt.subplot(313)
    plt.plot(x3)

    plt.show()

    for e,xx in enumerate([x1,x2,x3]): 
        scales, fluct, alpha = dfa(xx)
        print("DFA exponent {}: {}".format(e+1, alpha))
